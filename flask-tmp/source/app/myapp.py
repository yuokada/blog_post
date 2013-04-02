#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return "Hello world"

@app.route('/about')
def show_about():
    """ this is about page (static)
    """
    return "this is about world"

@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def show_users(user_id):
    """
        :param user_id: user id

        :query offset: offset
        :query  limit: limit
        :statuscode 200: OK
    """
    return "this is about world"

if __name__ == '__main__':
    app.run()
