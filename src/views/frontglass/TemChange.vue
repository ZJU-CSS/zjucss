<template>
  <div class="test-container">
    <div id="title">Climate spiral to show temperature change</div>
    <!-- TODO: 剪切视频，把这地方的图片换成视频 -->
    <video
      loop="loop"
      muted="muted"
      autoplay="autoplay"
      src="@/assets/frontglass/tem/TemChange.mp4"
      id="img"
    ></video>
    <div id="content">
      Say what you will about circular visualization, but the spiral plays. This
      one from NASA shows global temperature change over time: The visualization
      presents monthly global temperature anomalies between the years 1880-2021.
      These temperatures are based on the GISS Surface Temperature Analysis
      (GISTEMP v4), an estimate of global surface temperature change. Anomalies
      are defined relative to a base period of 1951-1980. The data file used to
      create this visualization can be accessed here. This is based on Ed
      Hawkins’ chart originally from 2016, but watch to the end for some extra
      sauce.
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
    font-size: 28px;
    line-height: 48px;
    text-indent: 2em;
    display: flex;
    align-items: center;
    color: #abb2bf;
  }
}
</style>
