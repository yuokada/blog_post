#!/usr/bin/env  python2.7
# -*- coding:utf-8 -*-
from flask import Flask, Response, json
from datetime import datetime
app = Flask(__name__)
app.config.from_pyfile('conf/app.cfg', silent=True)

@app.route('/name/<name>.json')
def hello_world(name):
    greet = u"こんにちわ %s from flask!" % name
    result = {
        "ResultSet": {
            "Result": {
                "Greeting": greet
            }
        }
    }

    response = Response(json.dumps(result))
    response.headers['Content-Type'] = "application/json"
    response.headers['Last-Modified'] = \
        datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')
    app.logger.debug(json.dumps(result))
    app.logger.debug(app.config["DATABASE"])
    return response

if __name__ == '__main__':
    app.run()
