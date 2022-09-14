<template>
  <div id="box">
    <div id="card-container">
      <el-card :body-style="{ padding: '1vw' }">
        <img
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          class="image"
          @click="test"
        />
        <div style="padding: 1vw" id="miaoshu">
          <p>标题</p>
          <el-button type="primary" class="button">打开浏览器</el-button>
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
          <el-button type="primary" class="button">打开浏览器</el-button>
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
          <el-button type="primary" class="button">打开浏览器</el-button>
        </div>
      </el-card>
      <el-button type="success" id="bt" @click="prev">上一页</el-button>
      <div id="space"></div>
      <el-button type="success" id="bt" @click="next">下一页</el-button>
      <el-card :body-style="{ padding: '1vw' }">
        <img
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          class="image"
          @click="test"
        />
        <div style="padding: 1vw" id="miaoshu">
          <p>标题</p>
          <el-button type="primary" class="button">打开浏览器</el-button>
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
          <el-button type="primary" class="button">打开浏览器</el-button>
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
          <el-button type="primary" class="button">打开浏览器</el-button>
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
    };
  },
  methods: {
    test() {
      this.$alert("这是一段内容", "标题名称", {
        center: true,
        callback: (action) => {
          this.$message({
            type: "info",
            message: `action: ${action}`,
          });
        },
      });
      setTimeout(() => {
        this.$msgbox.close();
      }, 2000);
    },
    next() {},
    prev() {},
    send(ip, content) {
      let url = this.List[ip];
      if (content === "open") {
        url += "open";
      } else {
        url = url + "url/" + content;
      }
      this.$axios.get(url).then((response) => {
        console.log(response);
      });
    },
  },
};
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
  #space {
    width: 50vw;
  }
  .el-card {
    .image {
      width: 100%;
      height: 24vw;
      display: block;
    }
    #miaoshu {
      display: flex;
      justify-content: space-between;
      align-items: center;
      .button {
        padding: 0.1vw;
        font-size: 1.3vw;
        height: a3vw;
        width: 35%;
      }
      p {
        font-size: 1.8vw;
        width: 60%;
        overflow: hidden;
      }
    }
  }
}
::v-deep {
  .el-card {
    height: 32vw;
    width: 25vw;
    margin: 5vw 1vw;
  }
  .el-button {
    font-size: 2.3vw;
    line-height: 2.3vw;
    margin: 0 !important;
  }
}
</style>
