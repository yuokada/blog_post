#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import dbm
import json
from flask import Flask, g, Response, request, abort
from flask.views import MethodView

app = Flask(__name__)

@app.before_request
def open_db():
    g.db = dbm.open('zip_local', 'c')


@app.after_request
def add_header(response):
    response.headers['Last-Modified'] = \
        "Wed, 21 Jun 2012 07:00:25 GMT"
    return response


@app.teardown_request
def close_db(e):
    """close_db"""
    g.db.close()


class ZipCodeAPI(MethodView):
    """docstring for ZipCode"""

    def __init__(self):
        super(ZipCodeAPI, self).__init__()
        print request.json

    def get(self, zipcode):
        data = g.db[str(zipcode)]
        keys = ['zipcode', 'prefecture', 'city', 'town']
        results = zip(keys, data.split(","))
        res = Response(json.dumps(dict(results)))
        res.headers["Content-Type"] = "application/json"
        return res

    def post(self, zipcode):
        if request.json:
            keys = ['zipcode', 'prefecture', 'city', 'town']
            request_keys = request.json.keys()

            row = []
            for k in keys[1:]:
                if k in request_keys:
                    row.append(request_keys[k])
                else:
                    abort(400)
            value = ",".join(row)
            print value
            #g.db[zipcode] = value
            res = Response("OK")
            res.headers['Content-Type'] = 'application/json'
            return res
        else:
            abort(400)

    def delete(self, zipcode):
        pass


zipcode_api = ZipCodeAPI.as_view('zipcode_api')
app.add_url_rule('/zipcode/<int:zipcode>.json', view_func=zipcode_api,
                 methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/zipcode/<int:zipcode>', view_func=zipcode_api,
                 methods=['GET', 'POST', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
