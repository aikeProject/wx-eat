const utils = require('../../utils/util.js')

const app = getApp()
Page({
  data: {
    userInfo: {},
    categories: [],
    categoryIndex: 0,
    food: ''
  },

  onShow: function() {
    // 判断是否登录
    var that = this
    wx.checkSession({
      success: function() {
        //session_key 未过期，并且在本生命周期一直有效
        that.setData({
          categories: wx.getStorageSync('categories')
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
  },

  // 菜系切换
  bindCateChange: function(e) {
    this.setData({
      categoryIndex: e.detail.value
    })
  },
  // 提交表单
  formSubmit: function(e) {
    var that = this
    var categories = wx.getStorageSync('categories')
    var categoryIndex = e.detail.value.categoryIndex
    var cate_id = categories[categoryIndex].id
    var food = e.detail.value.food
    if (!food) {
      wx.showToast({
        title: '请填写美食名称',
        icon: 'none'
      });
      return false;
    }

    utils.request('/api/food/foodAdd', 'post', {
      cate_id: cate_id,
      food: food
    }).then((res) => {
      this.setData({
        food: ''
      });
      wx.showToast({
        title: '添加成功',
        icon: 'success'
      });
    });

  }
})