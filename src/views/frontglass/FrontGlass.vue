<template>
  <div class="app">
    <div class="container" v-show="!this.flag">
      <img src="@/assets/frontglass/1.jpg" id="img1" />
      <!--      <TemChange v-show="this.count == 0" id="page1"></TemChange>-->
      <!--      <LiteracyScores v-show="this.count == 1" id="page1"></LiteracyScores>-->
      <!--      <VR v-show="this.count == 2" id="page1"></VR>-->
      <!--      <Page4 v-show="this.count == 3" id="page1"></Page4>-->
      <!--      <Page5 v-show="this.count == 4" id="page1"></Page5>-->
      <!--      <Page6 v-show="this.count == 5" id="page1"></Page6>-->
      <!--      <Page7 v-show="this.count == 6" id="page1"></Page7>-->
      <!--      <Page8 v-show="this.count == 7" id="page1"></Page8>-->
      <video src="@/assets/frontglass/video.mp4" muted="muted" autoplay loop class="video"></video>
      <iframe src="arxiv.html" frameborder="0" id="page2"></iframe>
      <img src="@/assets/frontglass/6.png" id="img2" />
    </div>
    <div class="test-container" v-show="this.flag">
      <welcome></welcome>
    </div>
  </div>
</template>

<script>
import Welcome from '@/views/frontglass/Welcome'
export default {
  components: {
    Welcome,
  },
  data() {
    return {
      flag: true,
      count: 0,
    }
  },
  methods: {},
  mounted() {
    this.timer = setInterval(() => {
      setTimeout(() => {
        this.flag = !this.flag
      }, 12000)
      this.flag = !this.flag
    }, 24000)
  },
  beforeDestroy() {
    clearInterval(this.timer)
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.app {
  position: relative;
}
.container {
  position: absolute;
  width: 4800px;
  height: 1280px;
  background-color: black;
  #img1 {
    position: absolute;
    left: 0;
    top: 190px;
    width: 800px;
    height: 900px;
  }
  #img2 {
    position: absolute;
    left: 4000px;
    top: 190px;
    width: 800px;
    height: 900px;
  }
  #page1 {
    position: absolute;
    left: 800px;
    top: 190px;
    width: 1600px;
    height: 900px;
  }
  #page2 {
    position: absolute;
    left: 2400px;
    top: 190px;
    width: 1600px;
    height: 900px;
  }
}
.test-container {
}
.video {
  position: absolute;
  left: 800px;
  top: 190px;
  width: 1600px;
  height: 900px;
}
</style>
