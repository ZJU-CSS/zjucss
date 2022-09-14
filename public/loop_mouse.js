window.onload = function () {
  function time_over() {
    return new Promise(resolve => {
      setTimeout(() => resolve('complete'), 6000)
    })
  }
  function time_click() {
    return new Promise(resolve => {
      setTimeout(() => resolve('complete'), 900)
    })
  }
  var loopOver = function () {
    obj2 = document.getElementsByClassName('slice')
    // console.log(obj2.innerHTML)

    var count2 = 0
    for (var j in obj2) if (obj2.hasOwnProperty(j)) count2++
    var random2 = Math.floor(Math.random() * (count2 - 0))
    var dom = document.getElementsByClassName('slice')[random2]

    var obj3 = dom.getElementsByTagName('text')
    if (obj3 !== '') {
    }
    // console.log(obj3[0].textContent)
    var evt = document.createEvent('MouseEvents')
    evt.initMouseEvent('mouseover', true, true, window, 0, 0, 0, 80, 20, false, false, false, false, 0, null)
    dom.dispatchEvent(evt)
    const result = time_over()
    result.then(loopClick)
  }
  var loopClick = function () {
    obj1 = document.getElementsByClassName('slice cursor-pointer')
    var count1 = 0
    for (var j in obj1) if (obj1.hasOwnProperty(j)) count1++
    var random1 = Math.floor(Math.random() * (count1 - 0))
    var dom = document.getElementsByClassName('slice')[random1]
    var evt = document.createEvent('MouseEvents')
    evt.initMouseEvent('click', true, true, window, 0, 0, 0, 80, 20, false, false, false, false, 0, null)
    dom.dispatchEvent(evt)
    const result = time_click()
    result.then(loopOver)
  }
  loopClick()
}
