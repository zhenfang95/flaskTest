# !/usr/bin/env Python3
# -*- coding:utf-8 -*-
# @Time : 2021/6/4 15:52

from flask import Blueprint
from flask import jsonify,request
from app.dao.auth.UserDao import UserDao
from app.handler.factory import ResponseFactory
from app.middleware.Jwt import UserToken

auth = Blueprint("auth",__name__,url_prefix="/auth")

#这里以auth.route注册的函数都会自带/auth，所以url是/auth/register
@auth.route("/register",methods=["POST"])
def register():
    #获取request请求数据
    data = request.get_json()
    username,password = data.get("username"),data.get("password")
    if not username or not password:
        return jsonify(dict(code=101,msg="用户名或密码不能为空"))
    email,name = data.get("email"),data.get("name")
    if not email or not name:
        return jsonify(dict(code=101,msg="姓名或邮箱不能为空"))
    err = UserDao.register_user(username,name,password,email)
    if err is not None:
        return jsonify(dict(code=110,msg=err))
    return jsonify(dict(code=0,msg="注册成功"))   #jsonify是flask自带的json处理类，返回的为flask结果

@auth.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    username,password = data.get("username"),data.get("password")
    if not username or not password:
        return jsonify(dict(code=101,msg="用户名或密码不能为空"))
    user,err = UserDao.login(username,password)  #login会返回两个结果
    if err is not None:
        return jsonify(dict(code=101,msg=err))
    user = ResponseFactory.model_to_dict(user,"password") #将user类转成dict
    token = UserToken.get_token(user)
    if err is not None:
        return jsonify(dict(code=110,msg=err))
    return jsonify(dict(code=0,msg="登陆成功",data=dict(token=token,user=user)))
