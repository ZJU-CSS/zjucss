import http from './http'
import { ipLists } from '@/constant/constants'
import { Message } from 'element-ui'

const ipChromeMap = {
  拼接屏1号机: false,
  拼接屏2号机: false,
  拼接屏3号机: false,
  拼接屏4号机: false,
  拼接屏5号机: false,
  弧形墙投影: false,
  外玻璃投影: false,
  窗户投影: false,
  test: false,
}
/**
 * 打开浏览器
 * @param {String}id
 * @return {Promise<void>}
 */
export async function openChrome(id) {
  const ip = ipLists[id]
  let res = await http({
    methods: 'get',
    url: ip + 'openChrome',
  })
  res = res.data
  if (res !== 'success') {
    const reg = /Current browser version is (\d+)./
    if (reg.test(res)) {
      Message.warning('正在更新ChromeDriver，请稍等~')
      const version = reg.exec(res)[1]
      let list = await http({
        methods: 'get',
        url: ip + 'getVersionList',
      })
      list = list.data
      for (let i = 0; i < list.length; i++) {
        if (list[i].name.startsWith(version)) {
          console.log(list[i].name)
          const url = list[i].url + 'chromedriver_win32.zip'
          let res = await http({
            method: 'post',
            data: {
              url,
            },
            url: ip + 'updateDriver',
          })
          if (res.data === 'success') {
            let res = await http({
              methods: 'get',
              url: ip + 'openChrome',
            })
            res = res.data
            if (res === 'success') {
              ipChromeMap[id] = true
              Message.success(id + '浏览器打开成功！')
            } else {
              Message.error('更新ChromeDriver错误，请手动更新')
            }
          } else {
            Message.error('更新ChromeDriver错误，请手动更新')
          }
          break
        }
      }
    } else {
      Message.error('未知错误！')
    }
  } else {
    ipChromeMap[id] = true
    Message.success(id + '浏览器打开成功！')
  }
}

/**
 * 切换对应内容
 * @param {String}id
 * @param {String}content
 * @return {Promise<void>}
 */
export async function openContent(id, content) {
  if (ipChromeMap[id] === false) {
    await openChrome(id)
  }
  const ip = ipLists[id]
  let res = await http({
    methods: 'get',
    url: ip + 'url/' + content,
  })
  res = res.data
  if (res === 'success') {
    Message.success(id + content + '打开成功！')
    switch (content) {
      case 'welcome':
        await clickScreen(10, 10, ip)
        break
    }
  }
}

/**
 * 点击屏幕播放内容
 * @param {Number}x
 * @param {Number}y
 * @param {String}ip
 * @return {Promise<void>}
 */
async function clickScreen(x, y, ip) {
  http({
    method: 'post',
    url: ip + 'playVideo',
    data: {
      x,
      y,
    },
  })
}
