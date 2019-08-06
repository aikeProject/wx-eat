//index.js
//获取应用实例
const util = require('../../utils/util.js')

const app = getApp()

Page({
  data: {
    userInfo: {},
    categories: [],
    categoryIndex: 0,
    btnText: '开始',
    isProcess: false,
    dishes: [],
    food: "今天吃什么呢？"
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function() {
    this.getCategory();
    this.getFood();
  },
  getCategory() {
    const list = wx.getStorageSync('categories') || [];

    if (list.length) {
      this.setData({
        categories: list
      });
    } else {
      util.request('/api/food/category', 'post')
        .then((res) => {
          if (res) {
            wx.setStorageSync('categories', res.list || []);

            this.setData({
              categories: res.list || []
            });
          }
        });
    }
  },
  getFood(cateId=0) {
    util.request('/api/food/list', 'post', {
      cateId
    }).then(res => {
      const list = res.list || [];
      console.log(res)
      if (list.length) {
        this.setData({
          dishes: list
        });
      }
    });
  },
  onShow() {
    // 判断是否登录
    var that = this
    wx.checkSession({
      success: function() {
        //session_key 未过期，并且在本生命周期一直有效
        that.setData({
          userInfo: app.globalData.userInfo
        });
        return;
      },
      fail: function() {
        // session_key 已经失效，需要重新执行登录流程
        wx.navigateTo({
          url: "../login/login"
        })
      }
    })
  }
})