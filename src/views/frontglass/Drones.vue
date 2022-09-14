<template>
  <div class="test-container">
    <div id="title">
      Drones Have Revolutionised Medical Deliveries in Rwanda
    </div>
    <img src="@/assets/frontglass/drones/1.png" alt="" id="img" />
    <div id="content">
      Getting medicine to remote parts of Africa isn’t easy. Drones change
      everything. Flying at 100km/h, they can cut a treacherous 4-hour road
      journey to just 30 minutes. Drones delivered 5,500 units of blood to
      Rwandan regional hospitals over a 12-month period. It led to a reduction
      in maternal deaths. Fewer cases of malaria-induced anaemia. Rwanda is
      leading the way.
    </div>
  </div>
</template>

<script>
export default {
  methods: {},
  mounted() {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.test-container {
  width: 1600px;
  height: 900px;
  position: relative;
  background-color: rgba(17, 17, 17);
  color: rgb(220, 203, 203);
  #title {
    position: absolute;
    top: 50px;
    left: 50%;
    width: 1600px;
    height: 50px;
    transform: translate(-50%, 0);
    text-align: center;
    font-size: 48px;
    line-height: 60px;
  }
  #sub-title {
    position: absolute;
    top: 130px;
    left: 50%;
    width: 1200px;
    height: 50px;
    font-style: italic;
    transform: translate(-50%, 0);
    text-align: center;
    font-size: 28px;
    line-height: 40px;
    color: rgb(126, 118, 118);
  }
  #img {
    position: absolute;
    right: 50px;
    top: 54%;
    transform: translate(0, -50%);
    width: 600px;
    height: 600px;
    display: flex;
    align-items: center;
  }

  #content {
    //background-color: orange;
    position: absolute;
    left: 50px;
    top: 150px;
    width: 800px;
    height: 700px;
    font-size: 32px;
    line-height: 56px;
    text-indent: 2em;
    display: flex;
    align-items: center;
    color: #abb2bf;
  }
}
</style>
