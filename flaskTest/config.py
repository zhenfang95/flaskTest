# !/usr/bin/env Python3
# -*- coding:utf-8 -*-
# @Time : 2021/6/4 14:30

import os

class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT,'logs','app.log')
    JSON_AS_ASCII = False #解决flask jsonify编码问题

    #Mysql连接信息
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = '123456'
    DBNAME = 'dev123'

    #sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
                                        MYSQL_USER,MYSQL_PWD,MYSQL_HOST,MYSQL_PORT,DBNAME)
    SQLALCHEMY_TRACK_NODIFICATIONS = False
