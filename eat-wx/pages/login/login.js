// pages/login/login.js
const util = require('../../utils/util.js')

const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    angle: 0
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {
    wx.onAccelerometerChange(res => {
      var angle = -(res.x * 30).toFixed(1);

      if (angle > 14) {
        angle = 14;
      } else if (angle < -14) {
        angle = -14;
      }

      if (this.data.angle !== angle) {
        this.setData({
          angle: angle
        });
      }
    });

    // 登录
    this.login()
  },

  login() {
    wx.getSetting({
      success: setting => {
        if (setting.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: user => {
              const userInfo = user.userInfo || {};

              wx.login({
                success: res => {
                  // 发送 res.code 到后台换取 openId, sessionKey, unionId
                  util.request('/api/user/login', 'post', {
                    code: res.code,
                    nickName: userInfo.nickName,
                    avatarUrl: userInfo.avatarUrl
                  }, {
                    authorization: false
                  }).then((data) => {
                    if (data) {
                      app.globalData.userInfo = data.userInfo;
                      wx.setStorageSync('token', data.token || '');

                      wx.switchTab({
                        url: '/pages/index/index',
                      });
                    }
                  });
                }
              });
            }
          })
        }
      }
    });
  }
})