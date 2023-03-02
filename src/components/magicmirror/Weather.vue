<template>
  <div id="container">
    <img :src="iconSrc" alt="" />
    <div>
      <p id="p1">{{ weather }}</p>
      <p id="p2">{{ temperature }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      temperature: 20 + '°C',
      weather: 'rain',
      iconSrc: 'http://openweathermap.org/img/wn/04n.png',
    }
  },
  methods: {
    getWeather() {
      this.$axios
        .get('http://api.openweathermap.org/data/2.5/weather?q=hangzhou&appid=7328419133fa6fd44868e923b84869d1')
        .then((response) => {
          this.temperature = Math.floor(response.data.main.temp - 273.15) + '°C'
          this.weather = response.data.weather[0].main
          this.iconSrc = 'http://openweathermap.org/img/wn/' + response.data.weather[0].icon + '.png'
        })
      // console.log(this.iconSrc)
    },
  },
  created() {
    this.getWeather()
    setInterval(() => {
      this.getWeather()
    }, 600000)
  },
}
</script>

<style lang="less" scoped>
#container {
  font-size: 3.6vw;
  width: 30vw;
  height: 10vw;
  color: white;
  position: relative;
  img {
    position: absolute;
    top: 0;
    left: 0;
    width: 10vw;
  }
  div {
    margin-left: 10vw;
  }
}
</style>
