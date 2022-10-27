<template>
  <div id="box">
    <div id="card-container">
      <el-button type="success" class="left-button" @click="prev">上一页</el-button>
      <el-button type="success" class="right-button" @click="next">下一页</el-button>
      <el-card :body-style="{ padding: '1vw' }">
        <img src="@/assets/magicmirror/content/ITS.png" class="image" @click="test" />
        <div class="title">网约车流量可视化</div>
        <el-button type="primary" class="button" size="small">切换内容</el-button>
      </el-card>
      <el-card :body-style="{ padding: '1vw' }">
        <img src="" class="image" @click="test" />
        <div style="padding: 1vw" id="miaoshu">
          <p>标题</p>
          <el-button type="primary" class="button">切换内容</el-button>
        </div>
      </el-card>
      <el-card :body-style="{ padding: '1vw' }">
        <img
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          class="image"
          @click="test"
        />
        <div style="padding: 1vw" id="miaoshu">
          <p>标题</p>
          <el-button type="primary" class="button">切换内容</el-button>
        </div>
      </el-card>
      <el-card :body-style="{ padding: '1vw' }">
        <img
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          class="image"
          @click="test"
        />
        <div style="padding: 1vw" id="miaoshu">
          <p>标题</p>
          <el-button type="primary" class="button">切换内容</el-button>
        </div>
      </el-card>
      <el-card :body-style="{ padding: '1vw' }">
        <img
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          class="image"
          @click="test"
        />
        <div style="padding: 1vw" id="miaoshu">
          <p>标题</p>
          <el-button type="primary" class="button">切换内容</el-button>
        </div>
      </el-card>
      <el-card :body-style="{ padding: '1vw' }">
        <img
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          class="image"
          @click="test"
        />
        <div style="padding: 1vw" id="miaoshu">
          <p>标题</p>
          <el-button type="primary" class="button">切换内容</el-button>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      List: [],
    }
  },
  methods: {
    test() {
      this.$alert('这是一段内容', '标题名称', {
        center: true,
        callback: (action) => {
          this.$message({
            type: 'info',
            message: `action: ${action}`,
          })
        },
      })
      setTimeout(() => {
        this.$msgbox.close()
      }, 2000)
    },
    next() {},
    prev() {},
    send(ip, content) {},
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
  justify-content: space-between;
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
  }
  .right-button {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
  }
  .left-button {
    position: absolute;
    top: 50%;
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
