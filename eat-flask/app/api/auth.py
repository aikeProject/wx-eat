#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   成雨
@Contact :   1121352970@qq.com
@Software:   PyCharm
@File    :   auth.py
@Time    :   2019-08-05 17:22
@Desc    :   Token 认证
"""
from flask import g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.api.errors import error_response
from app.models import User

token_auth = HTTPTokenAuth()
serializer = Serializer('chengyu')


@token_auth.verify_token
def verify_token(token):
    try:
        data = serializer.loads(token)  # 验证token
    except:
        return False
    if 'user_id' in data:
        user = User.query.filter_by(id=data['user_id']).first()
        if user:
            g.user = user
            return True
    return False


@token_auth.error_handler
def token_auth_error():
    return error_response(401)
