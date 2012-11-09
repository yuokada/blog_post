#!/usr/bin/env  python2.7
from flask import Flask, jsonify, after_this_request
app = Flask(__name__)

@app.route('/name/<name>.json')
def hello_world(name):
  greet = "Hello %s from flask!" % name
  result = {
    "Result":{
      "Greeting": greet
      }
  }
  @after_this_request
  def d_header(response):
      """ add header

      Arguments:
      - `response`:
      """
      response.headers['Last-Modified'] = \
        "Last-Modified: Wed, 21 Jun 2012 07:00:25 GMT"
      return response
  return jsonify(ResultSet=result)

if __name__ == '__main__':
    app.run(debug=True)
