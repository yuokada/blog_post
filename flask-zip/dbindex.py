#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import json
from flask import Flask, g, Response, request, abort
from flask.views import MethodView

from sqlalchemy import Column, Integer, Unicode, create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ZipCode(Base):
    __tablename__ = 'zipcodes'

    zipcode = Column(Integer, primary_key=True)
    prefecture = Column(Unicode)
    city       = Column(Unicode)
    town       = Column(Unicode)

    def __init__(self, zipcode, prefecture=None, city=None, town=None):

        self.zipcode = zipcode
        self.prefecture = prefecture
        self.city = city
        self.town = town

    def __repr__(self):
       return "<ZipCode(%d)>" % (self.zipcode)

app = Flask(__name__)

@app.before_first_request
def init_db():
    print "INIT DB! Yeahhh!"
    #engine = create_engine("sqlite:///local_zip.db")
    #metadata = MetaData(bind=engine)
    #Base.metadata = metadata
    #ZipCode.metadata.create_all()


@app.before_request
def add_session():
    engine = create_engine("sqlite:///local_zip.db", echo=True)
    Base.metadata.reflect(engine)
    db_session = scoped_session(sessionmaker(bind=engine))
    g.session = db_session


@app.after_request
def add_header(response):
    if response.status_code in [200, 201]:
        response.headers['Last-Modified'] = \
            "Wed, 21 Jun 2012 07:00:25 GMT"
        response.headers["Content-Type"] = "application/json"
    return response


@app.teardown_request
def remove_session(e):
    """ Remove session
    """
    g.session.remove()

class ZipCodeAPI(MethodView):

    def __init__(self):
        super(ZipCodeAPI, self).__init__()

    def get(self, zipcode):
        zip_ins = ZipCode(zipcode)
        q = g.session.query(ZipCode).filter_by(zipcode=zipcode)
        q_results = q.first()
        if not q_results:
            # レコードが見つからなかったので404で処理
            return abort(404)
        results = []
        keys = ['zipcode', 'prefecture', 'city', 'town']
        for k in keys:
            results.append((k, getattr(q_results, k)))
        res = Response(json.dumps(dict(results)))
        return res

    def post(self, zipcode):
        record = ZipCode(zipcode)
        # JSONリクエストでの更新を受け付ける
        if request.json:
            keys = ['zipcode', 'prefecture', 'city', 'town']
            request_keys = request.json.keys()
            for k in keys[1:]:
                if k in request_keys:
                    setattr(record, k, request.json[k])
                else:
                    abort(400)

            q = g.session.query(ZipCode).filter_by(zipcode=zipcode)
            res = q.first()
            #res = g.session.add(record)
            res = g.session.merge(record)
            g.session.commit()
            res = Response("OK")
            return res
        else:
            abort(400)

    def delete(self, zipcode):
        q_res = g.session.query(ZipCode).filter(ZipCode.zipcode==zipcode).delete()
        if q_res == 1:
            print "DELETE => Commit"
            print g.session.commit()
            response = Response("OK")
            response.status_code = 200
        else:
            print "Not Commit"
            print g.session.rollback()
            response =  Response("Not Found")
            response.status_code = 404
        return response


zipcode_api = ZipCodeAPI.as_view('zipcode_api')
app.add_url_rule('/zipcode/<int:zipcode>.json', view_func=zipcode_api,
                 methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/zipcode/<int:zipcode>', view_func=zipcode_api,
                 methods=['GET', 'POST', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)