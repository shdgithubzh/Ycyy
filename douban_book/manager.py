"""
@Created by Seven on 2018-04-17
import os
from flask import (Flask,request....)
"""

from douban_book.app import create_app

app = create_app('developments')

if __name__ == '__main__':
    app.run()
