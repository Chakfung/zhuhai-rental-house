# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from twisted.enterprise import adbapi
import pymysql

class ZhuhaiCrawlerPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    # from_settings after activate pipeline recall settings config
    @classmethod
    def from_settings(cls, settings):
        # database parameters
        db_params = dict(
            host=settings['MYSQL_HOST'],
            database=settings['MYSQL_database'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            charset='utf8mb4',
            use_unicode=True,
            cursorclass = pymysql.cursors.DictCursor
        )
        # create pool
        dbpool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(dbpool)
    
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_upsert, item)  
        query.addErrback(self.handle_error, item, spider)  
        return item

    # failure 
    def handle_error(self, failure, item, spider):
        print(failure)
    
    def do_upsert(self, cursor, item):
        upsert_sql = """insert into lianjia.spider(title,location,house_type,house_code,price,tags,lease,area,orientation,floor,elevator,stall,water,electricity,fuel_gas,heating,facility,description)
                        Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE latest_rent = CASE WHEN latest_rent <> VALUES(latest_rent) THEN VALUES(latest_rent) ELSE latest_rent END
                        , updated_time = CASE WHEN latest_rent <> VALUES(latest_rent) THEN now() ELSE updated_time END;"""
                        # when duplicated, check if rent changes, set newest rent into latest_rent field if changes, if not, stay as is
        cursor.execute(upsert_sql, (item['title'], item['location'], item['house_type'], item['house_code'], item['price'], item['tags'], item['lease'], item['area']
                                    , item['orientation'], item['floor'], item['elevator'], item['stall'], item['water'], item['electricity'], item['fuel_gas'], item['heating'], item['facility'], item['description'],
                                    ))
