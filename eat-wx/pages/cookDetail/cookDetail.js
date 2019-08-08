const utils = require('../../utils/util.js')

const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    id: null,
    info: [],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(option) {
    this.setData({
      id: option.id,
    })
    this.getCookDetail(option.id)
  },
  /**
   * 获取菜谱详细信息
   */
  getCookDetail: function(id) {
    var that = this
    utils.request('/api/food/cookDetail', 'post', {
      id: id
    }).then((res) => {
      this.setData({
        info: res
      })
    });
  },
  /**
   * 图片点击事件
   */
  imgYu: function(event) {
    var src = event.currentTarget.dataset.src; //获取data-src
    var imgList = event.currentTarget.dataset.list; //获取data-list
    //图片预览
    wx.previewImage({
      current: src, // 当前显示图片的http链接
      urls: imgList // 需要预览的图片http链接列表
    })
  }
})