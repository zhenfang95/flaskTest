#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2021/6/20 15:32

from flask import Blueprint
from flask import jsonify
from flask import request
from app.middleware.HttpClien import Request

req = Blueprint("request",__name__,url_prefix="/request")

@req.route("/http",methods=['POST'])
def http_request():
    data = request.get_json()
    method = data.get("method")
    if not method:
        return jsonify(dict(code=101,msg="请求方式不能为空"))
    url = data.get("url")
    if not url:
        return jsonify(dict(code=101, msg="请求地址不能为空"))
    body = data.get("body")
    headers = data.get("headers")
    response = Request(url,data=body,headers=headers).request(method)
    return jsonify(dict(code=0,data=response,msg="操作成功"))
