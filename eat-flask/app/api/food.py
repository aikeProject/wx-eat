#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   成雨
@Contact :   1121352970@qq.com
@Software:   PyCharm
@File    :   food.py
@Time    :   2019-08-05 15:30
@Desc    :
"""
import random

from flask import jsonify, request

from app.models import Category, Food
from app.utils.comm import json_response
from . import api
from app.api.auth import token_auth


@api.route('/food/category', methods=['POST'])
@token_auth.login_required
def get_category():
    """
    菜系列表
    """

    # 获取菜系信息，并根据order_number降序排序
    category = Category.query.order_by(Category.order_num.desc()).all()
    data = [{'id': 0, 'name': '全部'}]

    for item in category:
        data.append(
            {
                'id': item.id,
                'name': item.name
            }
        ),

    return jsonify(json_response(data={
        'list': data
    }))


@api.route('/food/list', methods=['POST'])
@token_auth.login_required
def get_food():
    """
    获取菜系信息
    """
    cate_id = int(request.values['cateId'])
    if cate_id:
        food = Food.query.filter_by(cate_id=cate_id).all()
    else:
        food = Food.query.all()
    data = []
    for item in food:
        data.append(item.name),

    # 乱序
    random.shuffle(data)

    return jsonify(json_response(data={
        'list': data
    }))
