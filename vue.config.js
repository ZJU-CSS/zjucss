const { defineConfig } = require('@vue/cli-service')
const path = require('path')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  publicPath: './',
  chainWebpack: (config) => {
    config.resolve.alias.set('@', resolve('src'))
  },
})
function resolve(dir) {
  return path.join(__dirname, dir)
}
