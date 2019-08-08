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

import requests
from flask import jsonify, request

from app import db
from app.models import Category, Food
from app.utils.comm import json_response
from config import Config
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


@api.route('/food/cookbook', methods=['POST'])
@token_auth.login_required
def get_cookbook():
    """
    菜谱列表
    """
    food = request.values['food']  # 接收传递过来的参数
    url = "http://apis.juhe.cn/cook/query.php"
    params = {
        "menu": food,  # 需要查询的菜谱名
        "key": Config.CookAppKey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json
        "pn": "0",  # 数据返回起始下标
        "rn": "5",  # 数据返回条数，最大30
        "albums": "",  # albums字段类型，1字符串，默认数组
    }
    response = requests.get(url=url, params=params)
    data_json = response.json()
    # 获取菜谱异常，返回异常信息
    if (data_json['resultcode'] != '200'):
        result = json_response(data_json['resultcode'], data_json['reason'])

        return jsonify(result)

    # 获取菜谱正常，返回菜谱信息
    data = []
    for item in data_json['result']['data']:
        data.append(
            {
                'id': item['id'],
                'title': item['title'],
                'imtro': item['imtro'],
                'albums': item['albums'][0]
            }
        )

    result = json_response(data_json['resultcode'], data_json['reason'], data={
        'list': data
    })

    return jsonify(result)


@api.route('/food/cookDetail', methods=['POST'])
@token_auth.login_required
def get_cook_detail():
    """
    菜谱详情
    """
    id = request.values['id']  # 接收传递过来的参数
    url = "http://apis.juhe.cn/cook/queryid"
    params = {
        "id": id,  # 菜谱的ID
        "key": Config.CookAppKey,  # 应用APPKEY
        "dtype": "",  # 返回数据的格式,xml或json，默认json
    }
    response = requests.get(url=url, params=params)
    data_json = response.json()
    # 获取菜谱异常，返回异常信息
    if (data_json['resultcode'] != '200'):
        result = json_response(data_json['resultcode'], data_json['reason'], {})
        return jsonify(result)

    # 获取菜谱正常，返回菜谱信息
    data = data_json['result']['data'][0]

    # 处理数据
    ingredients = []
    for item in data['ingredients'].split(';'):
        temp = {}
        name, consumption = item.split(',')
        temp['name'] = name
        temp['consumption'] = consumption
        ingredients.append(temp)
    burden = []
    for item in data['burden'].split(';'):
        temp = {}
        name, consumption = item.split(',')
        temp['name'] = name
        temp['consumption'] = consumption
        burden.append(temp)
    stepPics = []
    for item in data['steps']:
        stepPics.append(item['img'])

    info = {}
    info['title'] = data['title']
    info['albums'] = data['albums'][0]
    info['imtro'] = data['imtro']
    info['ingredients'] = ingredients
    info['burden'] = burden
    info['steps'] = data['steps']
    info['stepPics'] = stepPics

    result = json_response(data=info)
    return jsonify(result)


@api.route('/food/foodAdd', methods=['POST'])
@token_auth.login_required
def foodAdd():
    name = request.values['food']
    cate_id = request.values['cate_id']

    if cate_id == '0':
        result = json_response(201, '菜系不存在')
        return jsonify(result)

    try:
        food = Food.query.filter_by(name=name, cate_id=cate_id).first()
    except Exception as e:
        print(e)

    # 如果已经存在
    if food:
        result = json_response(201, '该美食已经存在')
    else:
        # 如果不存在，写入food表
        food = Food(
            name=name,
            cate_id=cate_id
        )
        db.session.add(food)
        db.session.commit()

        result = json_response()

    return jsonify(result)
