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
    keywords_url = 'https://api.douban.com/v2/book/search?q={}&count={}'

    @classmethod
    def search_by_keywords(cls, keywords, count=15):
        url = cls.keywords_url.format(keywords, count)
        result = HTTP.get(url=url)
        return result


class BookViewModel:
    """
    图书view
    """

    @classmethod
    def package_data(cls, data, keyword):
        res = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            res['total'] = 1
            res['books'] = [cls.__book_init_data(_book) for _book in data["books"]]
        return res

    @classmethod
    def __book_init_data(cls, data):
        book = {
            'title': data["title"],
            'author': data["author"],
            'image': data["image"]
        }

        return book
