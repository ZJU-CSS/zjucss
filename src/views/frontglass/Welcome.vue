<template>
  <div class="front_glass">
    <div class="logo">ZJUCSS</div>
    <div class="text">欢迎来到计算社会科学研究中心</div>
    <video autoplay loop muted src="../../assets/welcome.mp4"></video>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
}
</script>

<style scoped>
.front_glass {
  position: absolute;
  top: 0;
  left: 0;
  width: 4800px;
  height: 1280px;
  background-color: black;
}

.text {
  position: absolute;
  top: 54%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 100px;
  font-weight: bold;
  color: #fff;
  text-align: center;
  letter-spacing: 0.5em;
  z-index: 100;
  text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
}

.logo {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  position: absolute;
  top: 33%;
  left: 5%;
  z-index: 100;
  font-size: 50px;
  font-weight: bold;
  color: #fff;
  text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
}
video {
  position: absolute;
  overflow: hidden;
  width: 100%;
  height: 1100px;
  object-fit: cover;
  top: 0px;
  left: 0;
}
</style>
