<template>
  <div>
    <h2>拼接屏视频上传</h2>
    <el-upload class="upload-demo" drag action="#" :auto-upload="false" :on-change="uploadFile" :file-list="fileList">
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">
        只能上传单个 mp4 文件，上传后请根据位置自行查看 http://10.72.74.136:8887/video/1-1.mp4 (根据位置调整 1-1
        为其真实位置，如 3 号下为 3-2.mp4)，如无法打开请确认 MP4 编码格式，部分编码无法在 html
        中打开属正常现象，请转换编码格式。如上传问题可手动上传到 10.72.74.136 服务器，文件夹位置
        /home/zhiguangda/ITS/back/content_path_server/upload
        <br />
        大文件请手动上传，此处上传很可能失败
      </div>
    </el-upload>
    <div class="upload-line">
      <el-select v-model="val" placeholder="请选择">
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"> </el-option>
      </el-select>
      <el-button @click="handleUpload" type="primary" class="upload-btn" :disabled="!isUpload" :loading="loading"
        >上传</el-button
      >
    </div>
    <hr style="margin: 20px 0" />
    <h2>拼接屏页面</h2>
    <div class="btn-box">
      <el-button @click="openPage('http://10.72.74.136:5555/p1')" type="primary" style="margin: 10px 50px"
        >拼接屏 1 号：http://10.72.74.136:5555/p1</el-button
      >
      <el-button @click="openPage('http://10.72.74.136:5555/p2')" type="primary" style="margin: 10px 50px"
        >拼接屏 2 号：http://10.72.74.136:5555/p2</el-button
      >
      <el-button @click="openPage('http://10.72.74.136:5555/p3')" type="primary" style="margin: 10px 50px"
        >拼接屏 3 号：http://10.72.74.136:5555/p3</el-button
      >
      <el-button @click="openPage('http://10.72.74.136:5555/p4')" type="primary" style="margin: 10px 50px"
        >拼接屏 4 号：http://10.72.74.136:5555/p4</el-button
      >
      <el-button @click="openPage('http://10.72.74.136:5555/p5')" type="primary" style="margin: 10px 50px"
        >拼接屏 5 号：http://10.72.74.136:5555/p5</el-button
      >
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'upload',
  data() {
    return {
      loading: false,
      file: null,
      fileList: [],
      options: [
        {
          value: '1-1',
          label: '屏幕 1-上',
        },
        {
          value: '1-2',
          label: '屏幕 1-下',
        },
        {
          value: '2-1',
          label: '屏幕 2-上',
        },
        {
          value: '2-2',
          label: '屏幕 2-下',
        },
        {
          value: '3-1',
          label: '屏幕 3-上',
        },
        {
          value: '3-2',
          label: '屏幕 3-下',
        },
        {
          value: '4-1',
          label: '屏幕 4-上',
        },
        {
          value: '4-2',
          label: '屏幕 4-下',
        },
        {
          value: '5-1',
          label: '屏幕 5-上',
        },
        {
          value: '5-2',
          label: '屏幕 5-下',
        },
      ],
      val: '',
    }
  },
  mounted() {},
  computed: {
    isUpload() {
      return this.val && this.file
    },
  },
  methods: {
    uploadFile(file) {
      this.file = file
      this.fileList = [file]
      console.log(this.file)
    },
    openPage(url) {
      window.open(url)
    },
    handleUpload() {
      if (this.file?.raw?.type !== 'video/mp4') {
        this.$message.error('视频非 mp4 格式，请重新上传')
        this.file = null
        this.fileList = []
        return
      }
      this.loading = true
      const formData = new FormData()
      formData.append('file', this.file.raw)
      formData.append('index', this.val)
      axios
        .post('http://10.72.74.136:8887/upload', formData)
        .then((res) => {
          console.log('res:', res)
          this.$message({
            message: '上传成功，即将打开视频页面验证',
            type: 'success',
          })
          const ind = this.val
          setTimeout(() => {
            window.open('http://10.72.74.136:8887/video/' + ind + '.mp4')
          }, 3000)
        })
        .catch((e) => {
          this.$message.error('上传失败' + JSON.stringify(e))
        })
        .finally(() => {
          this.file = null
          this.val = ''
          this.loading = false
          this.fileList = []
        })
    },
  },
}
</script>

<style scoped lang="less">
h2 {
  margin: 10px 50px;
}
.upload-demo {
  margin: 50px;
}
.upload-line {
  margin: 0 50px;
}
.upload-btn {
  margin-left: 20px;
}
.btn-box {
  display: flex;
  flex-direction: column;
}
</style>
