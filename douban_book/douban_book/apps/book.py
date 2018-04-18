# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-17
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, jsonify, json)
from douban_book.helper import DoubanBook

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('/search/<q>/<int:start>/<int:count>/', methods=["GET"])
def index(q, start, count):
    """
    图书主页
    需要序列化 serializers
    :return:
    """
    if q and start is not None:
        result = DoubanBook.search_by_keywords(q, start, count)
        return jsonify(result)
        # return json.dumps(result), 200, {'content-type': 'application/json; charset=utf-8'}
