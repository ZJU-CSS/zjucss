<template>
  <div class="test-container">
    <div id="title">The generation game</div>
    <!-- TODO: 剪切视频，把这地方的图片换成视频 -->
    <img src="@/assets/frontglass/tem/tem.png" alt="" id="img" />
    <div id="content">
      Large, creative ai models will transform how people live and work. ChatGPT embodies more knowledge than any human
      has ever known. It can converse cogently about mineral extraction in Papua New Guinea, or about TSMC, a firm that
      finds itself in the geopolitical crosshairs. GPT­4, the artificial neural network which powers ChatGPT, has aced
      exams that serve as gateways for people to enter careers in law and medicine in America. It can generate songs,
      poems and essays. Other “generative AI” models can churn out digital photos, drawings and animations. Running
      alongside this excitement is deep concern, inside the tech industry and beyond, that generative AI models are
      being developed too quickly. GPT­4 is a type of generative AI called a large language model (LLM). Tech giants
      like Alphabet, Amazon and Nvidia have all trained their own LLMs, and given them names like PaLM, Megatron, Titan
      and Chinchilla. LLM have gone much further than anyone might have believed a few years ago. However you define
      AGI, AI researchers seem closer to it than they were a couple of years ago.
    </div>
  </div>
</template>

<script>
export default {
  methods: {},
  mounted() {},
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
