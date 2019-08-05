// pages/login/login.js
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
  onLoad: function (options) {
    
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    wx.onAccelerometerChange(res => {
      var angle = -(res.x * 30).toFixed(1);
      if (angle > 14) {
        angle = 14;
      }
      else if (angle < -14) {
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
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              console.log(res)
              // 登录
              wx.login({
                success: res => {
                  // 发送 res.code 到后台换取 openId, sessionKey, unionId
                  console.log(res)
                  setTimeout(() => {
                    wx.switchTab({
                      url: '/pages/index/index',
                    });
                  }, 500);

                }
              });
              
            }
          })
        }
      }
    });
  }
})