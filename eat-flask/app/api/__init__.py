#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   成雨
@Contact :   1121352970@qq.com
@Software:   PyCharm
@File    :   __init__.py.py
@Time    :   2019-08-05 15:23
@Desc    :   前台接口
"""

from flask import Blueprint

api = Blueprint("api", __name__)

from . import users, food, record
