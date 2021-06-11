# !/usr/bin/env Python3
# -*- coding:utf-8 -*-
# @Time : 2021/6/11 15:43

import datetime
import requests

class Request(object):
    def __init__(self,url,session=False,**kwargs):
        self.url = url
        self.session = session
        self.kwargs = kwargs
        if self.session:
            self.client = requests.session()
            return
        self.client = requests

    def get(self):
        return self.request("GET")

    @staticmethod
    def get_elapased(timer: datetime.timedelta):
        if timer.seconds > 0:
            return f"{timer.seconds}.{timer.microseconds // 1000}s"
        return f"{timer.microseconds // 100}ms"

    def request(self,method: str):
        status_code = 0
