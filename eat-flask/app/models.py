#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   成雨
@Contact :   1121352970@qq.com
@Software:   PyCharm
@File    :   models.py
@Time    :   2019-08-05 15:24
@Desc    :   ORM
"""

from . import db
from datetime import datetime


# 会员数据模型
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    openid = db.Column(db.String(50), )  # 微信用户id
    nickname = db.Column(db.String(100))  # 微信昵称
    phone = db.Column(db.String(11), unique=True)  # 手机号
    avatar = db.Column(db.String(200))  # 微信头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间

    def __repr__(self):
        return '<User %r>' % self.name

