<template>
  <div class="box">
    <div>111111</div>
  </div>
</template>

<script>
import { openChrome, openContent } from '@/api/api'
export default {
  name: 'test',
  data() {
    return {
      lists: [],
      url: '',
    }
  },
  async mounted() {
    openContent('test', 'ITS(融合2)')
    // this.$axios.post('http://10.211.55.4:7777/playVideo', {
    //   x: 495,
    //   y: 990
    // }).then(res => {
    //   this.test = res.data.slice(0, 10)
    //   console.log(this.test)
    // })
    // this.$axios.get('http://10.211.55.4:7777/openChrome').then(res => {
    //   res = res.data
    //   if(res !== 'success') {
    //     const reg = /Current browser version is (\d+)./
    //     const version = reg.exec(res)[1]
    //     console.log(version)
    // for (let i = 0; i < this.lists.length; i++) {
    //   if (this.lists[i].name.startsWith(version)) {
    //     console.log(this.lists[i].name)
    //     this.url = this.lists[i].url + 'chromedriver_win32.zip'
    //     this.$axios
    //       .post('http://10.211.55.4:7777/updateDriver', {
    //         url: this.url,
    //       })
    //       .then((res) => {
    //         if (res.data === 'success') {
    //           this.$axios.get('http://10.211.55.4:7777/openChrome')
    //         }
    //       })
    //     break
    //   }
    // }
    //   }
    // })
  },
}
</script>

<style scoped>
.box {
  color: white;
}
</style>
