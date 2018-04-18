# -*- coding:utf-8 -*-  
"""
@Created by Seven on 2018-04-17
import os
from flask import (Flask,request....)
"""
import requests


class HTTP:
    """
    封装requests
    静态方法直接通过类名去访问
    而非静态方法需要创建对象
    """
    @staticmethod
    def get(url, retuen_json=True):
        res = requests.get(url)
        if res.status_code != 200:
            return {'msg': 'book_not_found', 'code': '404'} if retuen_json else ''
        return res.json() if retuen_json else res.text


class DoubanBook:
    """
    检索豆瓣的图书
    """
    keywords_url = 'https://api.douban.com/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_keywords(cls, keywords, start=0, count=15):
        url = cls.keywords_url.format(keywords, start, count)
        result = HTTP.get(url=url)
        return result
