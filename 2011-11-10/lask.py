# -*- coding: utf-8 -*-
from flask import Flask, url_for, request, json, Response
app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/xml/articles/<articleid>', methods=['GET'], strict_slashes=False)
def api_xml_article(articleid):
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.args['format'] == 'json':
        js = json.dumps(request.args)
        resp = Response(js, status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://luisrei.com'
        return resp
    elif request.args['format'] == 'xml':
        xmldoc = '<?xml version="1.0" encoding="utf-8" ?><sample>エラーサンプル_1です。</sample>'
        resp = Response(xmldoc, status=200, mimetype='application/xml')
        resp.headers['Link'] = 'http://luisrei.com'
        return resp


if __name__ == '__main__':
    app.run(debug=True)
