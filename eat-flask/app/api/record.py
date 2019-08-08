#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   成雨
@Contact :   1121352970@qq.com
@Software:   PyCharm
@File    :   record.py
@Time    :   2019-08-05 15:30
@Desc    :
"""
from flask import request, g, jsonify

from app import db
from app.api.auth import token_auth
from app.models import Record
from app.utils.comm import json_response
from app.utils.errorCode import RECORD_ERR
from . import api


@api.route('/record/add', methods=["POST"])
@token_auth.login_required
def record_add():
    food = request.values['food']  # 获取美食ID
    user_id = g.user.id  # 获取用户ID
    record = Record.query.filter_by(user_id=user_id, food=food).first()
    try:
        if record:  # 如果记录已经存在，则更改选择美食次数
            record.number += 1
            db.session.add(record)
            db.session.commit()
        else:  # 如果记录不存在，则将美食次数设置为1
            record = Record(
                user_id=user_id,
                food=food,
                number=1
            )
            db.session.add(record)
            db.session.commit()
        result = json_response()
    except:
        result = json_response(*RECORD_ERR)
    return jsonify(result)


@api.route('/record/list', methods=["POST"])
@token_auth.login_required
def record_list():
    user_id = g.user.id
    record = Record.query.filter_by(user_id=user_id).all()
    if not record:
        return jsonify(json_response())
    data = []
    for item in record:
        temp = {
            "name": item.food,
            "value": item.number
        }
        data.append(temp)

    result = json_response(data={
        'list': data
    })
    return jsonify(result)


@api.route('/record/clear', methods=["POST"])
@token_auth.login_required
def record_clear():
    user_id = g.user.id
    try:
        Record.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        result = json_response(200, '清除数据成功')
    except:
        result = json_response(201, '清除数据失败')

    return jsonify(result)
