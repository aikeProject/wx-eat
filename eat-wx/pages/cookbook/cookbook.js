const utils = require('../../utils/util.js')

const app = getApp()
Page({
  data: {
    pageStatus: 'loading', // 加载标识
    food: null, //  美食名称
    cookbook: [] //  菜谱列表
  },
  onLoad: function(option) {
    this.setData({
      food: option.food, // 为页面变量赋值
    })
    this.getCookBook(option.food) // 调用获取菜谱方法
  },
  // 获取菜谱列表
  getCookBook: function(food) {
    this.setData({
      pageStatus: 'loading'
    })

    utils.request('/api/food/cookbook', 'post', {
      food: food
    }).then((res) => {
      this.setData({
        cookbook: res.list,
        pageStatus: 'done'
      })
    })
  },
  // 跳转首页方法
  goToIndex: function() {
    wx.switchTab({
      url: "../index/index"
    });
  }
})