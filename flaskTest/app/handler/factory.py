# !/usr/bin/env Python3
# -*- coding:utf-8 -*-
# @Time : 2021/6/7 21:00

from datetime import datetime

class ResponseFactory(object):
    @staticmethod
    def model_to_dict(obj,*ignore: str):   #ignore参数是一个可变字符串参数
        data = dict()
        for c in obj.__table__.columns:
            if c.name in ignore:
                # 如果字段忽略, 则不进行转换
                continue
            val = getattr(obj, c.name)
            if isinstance(val, datetime):
                data[c.name] = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                data[c.name] = val
        return data

    @staticmethod
    def model_to_list(data: list, *ignore: str):
        return [ResponseFactory.model_to_dict(x, *ignore) for x in data]