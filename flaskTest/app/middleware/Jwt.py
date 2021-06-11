# !/usr/bin/env Python3
# -*- coding:utf-8 -*-
# @Time : 2021/6/7 11:16

import hashlib
from datetime import timedelta,datetime
import jwt
from jwt.exceptions import ExpiredSignatureError

EXPIRED_HOUR = 3

class UserToken(object):
    key = 'testToken'
    salt = 'test'

    #jwt加密
    @staticmethod  #staticmethod 返回函数的静态方法
    def get_token(data):
        #把用户信息压缩成一串字符串，并设置「3小时」的过期时间
        new_data = dict({"exp":datetime.utcnow() + timedelta(hours=EXPIRED_HOUR)},**data)
        token = jwt.encode(new_data, key=UserToken.key).encode()
        return token.decode()

    #jwt解密
    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token,key=UserToken.key)  #解析用户信息
        except ExpiredSignatureError:
            raise Exception("token已过期，请重新登陆")

    @staticmethod
    def add_salt(password):     #密码加密
        m = hashlib.md5()
        bt = f"{password}{UserToken.salt}".encode("utf-8")
        m.update(bt)
        return m.hexdigest()