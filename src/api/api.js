import http from './http'
import { ipLists } from '@/constant/constants'
import { Message } from 'element-ui'

let sendlist1 = [
  'http://192.168.0.161:7777/url/交通1号',
  'http://192.168.0.143:7777/url/交通2号',
  'http://192.168.0.165:7777/url/交通3号',
  'http://192.168.0.173:7777/url/交通4号',
  'http://192.168.0.197:7777/url/交通5号',
]
let sendlist2 = [
  'http://192.168.0.161:7777/url/conclustion',
  'http://192.168.0.143:7777/url/MIC',
  'http://192.168.0.165:7777/url/ML',
  'http://192.168.0.173:7777/url/DTW',
  'http://192.168.0.197:7777/url/news',
]

const ipChromeMap = {
  拼接屏1号机: true,
  拼接屏2号机: true,
  拼接屏3号机: true,
  拼接屏4号机: true,
  拼接屏5号机: true,
  弧形墙投影: true,
  外玻璃投影: true,
  窗户投影: true,
  test: true,
}
/**
 * 打开浏览器
 * @param {String}id
 * @return {Promise<void>}
 */
export async function openChrome(id) {
  try {
    const ip = ipLists[id]
    let res = await http({
      methods: 'get',
      url: ip + 'openChrome',
    })
    res = res.data
    if (res == 'error') {
      Message.error(id + '出现未知错误')
      ipChromeMap[id] = false
    } else if (res == 'success') {
      Message.success(id + '打开浏览器成功')
      ipChromeMap[id] = true
    }
  } catch (e) {
    Message.error(id + '出现未知错误')
    ipChromeMap[id] = false
  }
}

/**
 * 切换对应内容
 * @param {String}id
 * @param {String}content
 * @return {Promise<void>}
 */
export async function openContent(id, content) {
  try {
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
      await clickScreen(10, 10, ip)
    } else {
      Message.error(id + content + '打开失败！')
    }
  } catch (e) {
    Message.error(id + content + '打开失败！')
  }
}

export function openPinjie1() {
  sendlist1.forEach((item) => {
    http({
      methods: 'get',
      url: item,
    })
      .then((res) => {
        if (res === 'success') {
          Message.success('打开成功')
        } else {
          Message.error('打开失败')
        }
      })
      .catch((res) => {
        Message.error('打开失败')
      })
  })
}

export function openPinjie2() {
  sendlist2.forEach((item) => {
    http({
      methods: 'get',
      url: item,
    })
      .then((res) => {
        if (res === 'success') {
          Message.success('打开成功')
        } else {
          Message.error('打开失败')
        }
      })
      .catch((res) => {
        Message.error('打开失败')
      })
  })
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
