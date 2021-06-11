# !/usr/bin/env Python3
# -*- coding:utf-8 -*-
# @Time : 2021/6/3 19:01

from flask import Flask
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app,supports_credentials=True)

app.config.from_object(Config)

