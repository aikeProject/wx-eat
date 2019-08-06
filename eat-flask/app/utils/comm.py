#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   成雨
@Contact :   1121352970@qq.com
@Software:   PyCharm
@File    :   comm.py
@Time    :   2019-08-05 16:52
@Desc    :
"""


def json_response(status=200, message='', data=None):
    data = data if isinstance(data, dict) else {}

    return {
        'status': status,
        'message': message,
        'data': data
    }
