const { defineConfig } = require('@vue/cli-service')
const path = require('path')
module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
  transpileDependencies: true,
  lintOnSave: false,
  // chainWebpack: (config) => {
  //   config.resolve.alias.set('@', resolve('src'))
  // },
})
function resolve(dir) {
  return path.join(__dirname, dir)
}
