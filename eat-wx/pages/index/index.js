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
        wx.navigateTo({
          url: "../login/login"
        })
      }
    });
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
  getFood(cateId = 0) {
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
  // 菜系切换
  bindCateChange: function(e) {
    this.setData({
      categoryIndex: e.detail.value
    })
    this.getFood(this.data.categories[e.detail.value].id)
  },
  // 开始和暂停按钮
  bindClickTap: function() {
    var that = this
    clearInterval(this.data.timer);
    if (this.data.isProcess) {
      this.setData({
        isProcess: false,
        btnText: "开始！"
      })
      wx.showModal({
        title: '成功！',
        content: '今天就吃' + that.data.food + "！",
        confirmText: "好！",
        cancelText: "换一个",
        success: function(res) {
          if (res.confirm) {
            that.record(that.data.food)
            wx.navigateTo({
              url: '../choose/choose?keyword=' + that.data.food
            })
          } else if (res.cancel) {
            console.log('用户点击取消')
          }
        }
      })
    } else {
      this.setData({
        isProcess: true,
        btnText: "停！"
      })
      var newDishes = this.data.dishes
      this.data.timer = setInterval(function() {
        var randomIndex = Math.floor((Math.random() * 100 % newDishes.length)) // 生成随机下标
        that.setData({
          food: newDishes[randomIndex],
        })
      }, 10);
    }
  },
  // 记录选择的美食
  record: function(food) {

    util.request('/api/record/add', 'post', {
      food: food
    }).then(res => {
      const list = res.list || [];
      console.log(res)
      if (list.length) {
        this.setData({
          dishes: list
        });
      }
    });
  }
})