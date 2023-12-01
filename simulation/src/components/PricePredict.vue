<template>
  <div class="PricePredict">
    <el-row>
      <el-col :span="24"
        ><div class="grid-content bg-purple-dark">
          <div class="title">Zhuhai Rent Predict</div>
          <el-form ref="form" :model="form" label-width="100px">
            <el-form-item label="Area">
              <el-input class="input" v-model="form.area"></el-input
              ><span class="house-type-span"> square</span>
            </el-form-item>
            <el-form-item label="Floor">
              <el-input class="input" v-model="form.floor"></el-input>
            </el-form-item>
            <el-form-item label="House Type">
              <span class="house-type-span">bedroom</span>
              <el-input class="input" v-model="form.bedroom"></el-input
              ><span class="house-type-span"> living room</span>
              <el-input class="input" v-model="form.livingRoom"></el-input>
              <span class="house-type-span"> bathroom </span>
              <el-input class="input" v-model="form.bathroom"></el-input>
            </el-form-item>
            <el-form-item label="District">
              <el-select
                v-model="form.district"
                placeholder="please choose distrcit"
              >
                <el-option
                  label="Doumen District"
                  value="Doumen District"
                ></el-option>
                <el-option
                  label="Hengqin District"
                  value="Hengqin District"
                ></el-option>
                <el-option
                  label="High-Tech District"
                  value="High-Tech District"
                ></el-option>
                <el-option
                  label="Jinwan District"
                  value="Jinwan District"
                ></el-option>
                <el-option
                  label="Xiangzhou District"
                  value="Xiangzhou District"
                ></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="Elevator">
              <el-switch v-model="form.elevator"></el-switch>
            </el-form-item>
            <el-form-item label="Fuel Gas">
              <el-switch v-model="form.fuelGas"></el-switch>
            </el-form-item>
            <el-form-item label="Indoor Facilities">
              <el-checkbox-group v-model="form.indoorFacilities">
                <span class="icon iconfont">&#xe725;</span>
                <el-checkbox
                  label="Washing Machine"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont">&#xe724;</span>
                <el-checkbox
                  label="Air Conditioner"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont">&#xea70;</span>
                <el-checkbox
                  label="Wardrobe"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont">&#xe7fa;</span>
                <el-checkbox
                  label="Television"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont">&#xe698;</span>
                <el-checkbox
                  label="Refrigerator"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont water-heater">&#xe73f;</span>
                <el-checkbox
                  label="Water Heater"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont">&#xeb66;</span>
                <el-checkbox label="Bed" name="indoorFacilities"> </el-checkbox>
                <span class="icon iconfont">&#xe608;</span>
                <el-checkbox
                  label="Heating"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont">&#xe6a2;</span>
                <el-checkbox
                  label="Broadband"
                  name="indoorFacilities"
                ></el-checkbox>
                <span class="icon iconfont">&#xe60e;</span>
                <el-checkbox
                  label="Natural Gas"
                  name="indoorFacilities"
                ></el-checkbox>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item label="Electricity">
              <el-radio-group v-model="form.electricity">
                <el-radio label="Commerce Electricity"></el-radio>
                <el-radio label="Civilian Electricity"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="Water">
              <el-radio-group v-model="form.water">
                <el-radio label="Commerce Water"></el-radio>
                <el-radio label="Civilian Water"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">submit</el-button>
              <el-button @click="claerInfo">clear</el-button>
            </el-form-item>
          </el-form>
        </div></el-col
      >
    </el-row>
  </div>
</template>

<script>
export default {
  name: "PricePredict",
  props: {
    // msg: String,
  },
  data() {
    return {
      form: {
        area: "",
        floor: "",
        bedroom: "",
        livingRoom: "",
        bathroom: "",
        district: "",
        elevator: false,
        fuelGas: false,
        electricity: "",
        water: "",
        indoorFacilities: [],
      },
      price: "",
    };
  },
  methods: {
    onSubmit() {
      if (
        !this.form.area ||
        !this.form.floor ||
        !this.form.bedroom ||
        !this.form.livingRoom ||
        !this.form.bathroom ||
        !this.form.district ||
        !this.form.water ||
        !this.form.electricity
      ) {
        this.$message({
          showClose: true,
          message: "Please fill out the form.",
        });
      } else {
        console.log(this.form.district);
        this.price = Math.floor(
          this.predictPrice(
            parseInt(this.form.area),
            this.form.electricity === "Commerce Electricity" ? 0 : 1,
            this.form.elevator ? 1 : 0,
            parseInt(this.form.floor),
            this.form.fuelGas ? 1 : 0,
            this.form.water === "Commerce Water" ? 0 : 1,
            parseInt(this.form.bedroom),
            parseInt(this.form.livingRoom),
            parseInt(this.form.bathroom),
            this.form.indoorFacilities.includes("Washing Machine") ? 1 : 0,
            this.form.indoorFacilities.includes("Air Conditioner") ? 1 : 0,
            this.form.indoorFacilities.includes("Wardrobe") ? 1 : 0,
            this.form.indoorFacilities.includes("Television") ? 1 : 0,
            this.form.indoorFacilities.includes("Refrigerator") ? 1 : 0,
            this.form.indoorFacilities.includes("Water Heater") ? 1 : 0,
            this.form.indoorFacilities.includes("Bed") ? 1 : 0,
            this.form.indoorFacilities.includes("Heating") ? 1 : 0,
            this.form.indoorFacilities.includes("Broadband") ? 1 : 0,
            this.form.indoorFacilities.includes("Natural Gas") ? 1 : 0,
            this.form.district
          )
        );
        this.$alert(this.price, "Predict Price", {
          confirmButtonText: "Close",
          callback: () => {},
        });
      }
    },
    claerInfo() {
      (this.form.area = ""),
        (this.form.floor = ""),
        (this.form.bedroom = ""),
        (this.form.livingRoom = ""),
        (this.form.bathroom = ""),
        (this.form.district = ""),
        (this.form.elevator = false),
        (this.form.fuelGas = false),
        (this.form.electricity = ""),
        (this.form.water = ""),
        (this.form.indoorFacilities = []);
    },
    predictPrice(
      area,
      electricity,
      elevator,
      floor,
      fuel_gas,
      water,
      bedroom,
      living_room,
      bathroom,
      washing_machine,
      air_conditioner,
      wardrobe,
      television,
      refrigerator,
      water_heater,
      bed,
      heating,
      broadband,
      natural_gas,
      district
    ) {
      const coefficients = {
        intercept: 943.8428797033107,
        area: 30.428346,
        electricity: -87.242346,
        elevator: 78.518876,
        floor: 11.977505,
        fuel_gas: 145.242987,
        water: -367.167757,
        bedroom: 79.017383,
        "living room": 514.35985,
        bathroom: 82.373385,
        "Washing Machine": -84.367002,
        "Air Conditioner": -71.662535,
        Wardrobe: -125.300425,
        Television: 182.750708,
        Refrigerator: 146.004075,
        "Water Heater": -99.820121,
        Bed: -46.602452,
        Heating: 167.745168,
        Broadband: 55.104968,
        "Natural Gas": 144.230935,
        "district_Doumen District": -1130.70217,
        "district_Hengqin District": 1289.862982,
        "district_High-Tech District": -8.756755,
        "district_Jinwan District": -585.144251,
        "district_Xiangzhou District": 434.740194,
      };

      let price = coefficients["intercept"];
      price += coefficients["area"] * area;
      price += coefficients["electricity"] * electricity;
      price += coefficients["elevator"] * elevator;
      price += coefficients["floor"] * floor;
      price += coefficients["fuel_gas"] * fuel_gas;
      price += coefficients["water"] * water;
      price += coefficients["bedroom"] * bedroom;
      price += coefficients["living room"] * living_room;
      price += coefficients["bathroom"] * bathroom;
      price += coefficients["Washing Machine"] * washing_machine;
      price += coefficients["Air Conditioner"] * air_conditioner;
      price += coefficients["Wardrobe"] * wardrobe;
      price += coefficients["Television"] * television;
      price += coefficients["Refrigerator"] * refrigerator;
      price += coefficients["Water Heater"] * water_heater;
      price += coefficients["Bed"] * bed;
      price += coefficients["Heating"] * heating;
      price += coefficients["Broadband"] * broadband;
      price += coefficients["Natural Gas"] * natural_gas;

      const districtCoefficient = coefficients[`district_${district}`] || 0;
      price += districtCoefficient;

      return price;
    },
  },
};
</script>

<style scoped>
.input {
  width: 100px;
}
.house-type-span {
  color: aliceblue;
  padding-right: 5px;
}
.PricePredict {
  margin-top: 100px;
  margin-bottom: 100px;
}
.title {
  width: 100%;
  display: flex;
  justify-content: center;
  padding-bottom: 20px;
  font-size: 28px;
  color: rgb(0, 56, 66);
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  max-width: 1000px;
  min-width: 800px;
  border-radius: 20px;
  padding: 20px;
  background: rgba(101, 191, 191, 0.831);
}
.iconfont {
  font-size: 24px;
  font-weight: 400;
  padding-right: 5px;
}
</style>
