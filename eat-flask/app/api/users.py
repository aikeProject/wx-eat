#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   成雨
@Contact :   1121352970@qq.com
@Software:   PyCharm
@File    :   users.py
@Time    :   2019-08-05 15:29
@Desc    :
"""
from flask import request, jsonify

from app import db
from app.api.auth import serializer
from app.libs.MemberService import MemberService
from app.models import User
from app.utils.comm import json_response
from app.utils.errorCode import WX_CODE_ERR, WX_SERVER_ERR
from . import api


@api.route('/user/login', methods=['POST'])
def login():
    """
    授权登录
    """

    req = request.values
    # 昵称
    nickname = req['nickName'] if 'nickName' in req else ''
    # 头像
    avatarUrl = req['avatarUrl'] if 'avatarUrl' in req else ''
    code = req['code'] if 'code' in req else ''

    if not code or len(code) < 1:
        return jsonify(json_response(*WX_CODE_ERR))

    openid = MemberService.getWeChatOpenId(code)

    if not openid:
        return jsonify(json_response(*WX_SERVER_ERR))

    user = User.query.filter_by(openid=openid).first()

    if not user:
        user = User(
            openid=openid,
            nickname=nickname,
            avatar=avatarUrl
        )

        db.session.add(user)
        db.session.commit()

    # 生成
    token = serializer.dumps({'user_id': user.id})

    result = json_response(data={
        "userInfo": {
            "nickName": user.nickname,
            "avatarUrl": user.avatar
        },
        "token": token.decode(),  # byte 转化为string
    })

    return jsonify(result)
