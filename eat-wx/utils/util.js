const BASE_URL = 'http://127.0.0.1:5000'

const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

function request(
  url = '',
  method = 'get',
  data = {},
  options = {}) {
  return new Promise((resolve, reject) => {
    const req = {};
    const opt = {
      type: '',
      header: null,
      authorization: true
    };
    method = method.toLowerCase();
    options = Object.assign({}, opt, options);

    req.url = BASE_URL + url;
    req.data = data;
    req.method = method;
    if (method === 'post') {
      if (options.header) {
        req.header = header;
      } else if (options.type === 'json') {
        req.header = {
          'content-type': 'application/json'
        };
      } else {
        req.header = {
          'content-type': 'application/x-www-form-urlencoded'
        };
      }
    }

    if (options.authorization) {
      req.header['Authorization'] = 'Bearer ' + wx.getStorageSync('token');
    }

    req.success = function(res) {
      const data = res.data;

      if (data.status === 200) {
        resolve(data.data, res);
      } else {
        wx.showToast({
          title: data.message || '网络繁忙，请稍后重试',
          icon: 'none',
          duration: 2000
        });
        reject(res);
      }
    }

    req.fail = function(res) {
      reject(res);
    }

    wx.request(req);
  })
}

module.exports = {
  formatTime: formatTime,
  request: request,
}