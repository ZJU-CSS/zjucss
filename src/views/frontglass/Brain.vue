<template>
  <div class="test-container">
    <div id="title">
      The first reference charts for the human brain have been completed
    </div>
    <div id="sub-title">
      They could become a useful tool in tracking healthy（and unhealthy）ageing
    </div>
    <img src="@/assets/frontglass/brain/1.jpg" alt="" id="img" />
    <div id="content">
      Reference charts are an important tool in modern primary medicine,
      covering many aspects of a person’s healthy development. There is,
      however, a big gap in their coverage: the human brain. Richard Bethlehem
      and Simon White from the University of Cambridge and Jakob Seidlitz from
      the University of Pennsylvania want to fix that. Writing in Nature, the
      neuroscientists describe the most comprehensive effort yet to create a
      standard against which someone’s brain development can be measured through
      their lifetime.
    </div>
  </div>
</template>

<script>
export default {
  methods: {},
  mounted() {}
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
  #sub-title {
    position: absolute;
    top: 130px;
    left: 50%;
    width: 1200px;
    height: 50px;
    font-style: italic;
    transform: translate(-50%, 0);
    text-align: center;
    font-size: 28px;
    line-height: 40px;
    color: rgb(126, 118, 118);
  }
  #img {
    position: absolute;
    right: 50px;
    top: 54%;
    transform: translate(0, -50%);
    width: 600px;
    height: 400px;
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
    font-size: 24px;
    line-height: 40px;
    text-indent: 2em;
    display: flex;
    align-items: center;
    color: #abb2bf;
  }
}
</style>
