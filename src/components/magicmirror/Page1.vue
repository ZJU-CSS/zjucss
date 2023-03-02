<template>
  <div id="box">
    <div id="card-container">
      <el-button type="success" class="left-button" @click="prev" v-if="nowPage === 2">上一页</el-button>
      <el-button type="success" class="right-button" @click="next" v-if="nowPage === 1">下一页</el-button>
      <el-card :body-style="{ padding: '1vw' }" v-for="item in list" :key="item.id" @click.native="mySend(item.id)">
        <img :src="item.imgSrc" class="image" />
        <div class="title">{{ item.name }}</div>
        <el-button type="primary" class="button" size="small">切换内容</el-button>
      </el-card>
    </div>
  </div>
</template>

<script>
import { openContent, openPinjie1, openPinjie2 } from '@/api/api.js'
import { contentList } from '@/constant/constants'
export default {
  data() {
    return {
      nowPage: 1,
    }
  },
  methods: {
    mySend(id) {
      switch (id) {
        case '拼接1':
          openPinjie1()
          break
        case '拼接2':
          openPinjie2()
          break
        case 'ITS(融合2)':
          openContent('弧形墙投影', 'ITS(融合2)')
          break
        case '音乐':
          openContent('弧形墙投影', '音乐')
          break
        case '疫情视频(融合4)':
          openContent('弧形墙投影', '疫情视频(融合4)')
          break
        case 'frontglass':
          openContent('外玻璃投影', 'frontglass')
          break
        case '海报':
          openContent('外玻璃投影', '海报')
          break
        case 'Kmeans':
          openContent('弧形墙投影', 'Kmeans')
          break
        case 'NASA':
          openContent('弧形墙投影', 'NASA')
          break
        case 'windMap':
          openContent('弧形墙投影', 'windMap')
          break
        case 'welcome':
          openContent('外玻璃投影', 'welcome')
          break
      }
    },
    next() {
      this.nowPage++
    },
    prev() {
      this.nowPage--
    },
  },
  computed: {
    list() {
      if (this.nowPage === 1) {
        return contentList.slice(0, 6)
      } else {
        return contentList.slice(6, 12)
      }
    },
  },
}
</script>

<style lang="less" scoped>
#card-container {
  display: flex;
  flex-wrap: wrap;
  height: 100%;
  width: 90%;
  margin: 0 auto;
  align-items: center;
  position: relative;
  #space {
    width: 50vw;
  }
  .el-card {
    position: relative;
    .image {
      width: 100%;
      height: 24vw;
      display: block;
      object-fit: contain;
      background-color: black;
    }
    .title {
      margin-top: 0.8vw;
      font-size: 1.8vw;
    }
    .button {
      position: absolute;
      right: 5%;
      bottom: 5px;
    }
    &:not(:nth-child(3n)) {
      margin-right: 2vw;
    }
  }
  .right-button {
    position: absolute;
    top: 53%;
    right: 10px;
    transform: translateY(-50%);
  }
  .left-button {
    position: absolute;
    top: 53%;
    left: 10px;
    transform: translateY(-50%);
  }
}
::v-deep {
  .el-card {
    height: 32vw;
    width: 25vw;
    margin: 5vw 1vw;
  }
  //.el-button {
  //  font-size: 2.3vw;
  //  line-height: 2.3vw;
  //  margin: 0 !important;
  //}
}
</style>
