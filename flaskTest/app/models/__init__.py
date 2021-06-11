# !/usr/bin/env Python3
# -*- coding:utf-8 -*-
# @Time : 2021/6/4 19:16

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)   #将app赋给SQLAlchemy从而生成一个db对象