<template>
  <div id="app">
    <PricePredict />
  </div>
</template>

<script>
import PricePredict from "./components/PricePredict.vue";

export default {
  name: "App",
  components: {
    PricePredict,
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  background-position: center;
  background-size: 100% 100%;
  background-repeat: no-repeat;
  background-image: url("https://img.zcool.cn/community/01271e5ca31134a801208f8b2600aa.jpg@2o.jpg");
}
</style>
