<template>
  <div id="box">
    <div id="title">魔镜: 实验室控制中心</div>
    <div id="info">
      <clock id="clock"></clock>
      <weather></weather>
    </div>
    <div id="tip">轻触图片即可切换内容</div>
    <router-view id="page"></router-view>
    <img src="@/assets/magicmirror/R.png" alt="" id="bgc" />
    <img src="@/assets/magicmirror/xt1.png" alt="" id="xt1" />
    <img src="@/assets/magicmirror/xt2.png" alt="" id="xt2" />
    <img src="@/assets/magicmirror/zjucss.png" alt="" id="zjucss" />
  </div>
</template>

<script>
import clock from '@/components/magicmirror/FlipClock.vue'
import weather from '@/components/magicmirror/Weather.vue'
export default {
  components: {
    clock,
    weather
  }
}
</script>

<style lang="less" scoped>
* {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  background-color: #091921;
  //background-color: rgb(3, 35, 60);
  height: 100vh;
  #box {
    padding: 5vw 3vw;
    height: calc(100vh - 10vw);
    #title {
      height: 5vw;
      text-align: center;
      color: white;
      font-size: 5vw;
      line-height: 5vw;
      padding-top: 5vw;
    }
    #info {
      margin-top: 8vw;
      height: 10vw;
      display: flex;
      justify-content: space-around;
      #clock {
        overflow: hidden;
        width: 50vw;
        height: 10vw;
      }
    }
    #tip {
      height: 5vw;
      text-align: center;
      color: white;
      font-size: 3vw;
      line-height: 3vw;
      padding-top: 12vw;
      font-style: italic;
    }
    #page {
      height: calc(100vh - 78vw);
      min-height: 15vw;
      position: relative;
      overflow-y: scroll;
      z-index: 5;
    }
    #bgc {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: transparent;
      z-index: 3;
    }
    #xt1 {
      position: fixed;
      top: 2.6vw;
      right: 1.8vw;
      width: 40vw;
      height: 35vw;
      background: transparent;
    }
    #xt2 {
      position: fixed;
      bottom: 2.5vw;
      left: 2.5vw;
      width: 30vw;
      height: 25vw;
      background: transparent;
    }
    #zjucss {
      position: fixed;
      top: 16vw;
      left: 5vw;
      width: 24vw;
      height: 5vw;
      background: transparent;
    }
  }
}

</style>
