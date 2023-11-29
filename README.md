# Zhuhai-rental-house
### execution steps

1. Create virtual environment
   ```sh
   python -m venv venv
   ```

2. activate venv
   ```sh
   ./venv/Script/activate
   ```
   
3. Install libraries    
   ```sh
   pip install -r requirements.txt
   ```
4. run crawler 
   ```sh
   cd zhuhai_crawler
   ```
   Because crawling takes a long time, it is recommended that you use the "output.csv" dataset in the root directory
   ```sh
   scrapy crawl zhuhai -o ../output.csv
   ```
5. data analysis part run analyse.ipynb in the root directory(use venv).
In map visualization part,
6. simulation part
    python version: simulation.ipynb
    web version:
    ```sh
    cd web_simulation
    ```