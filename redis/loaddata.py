#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import redis
import msgpack
from random import randint
import datetime


def create_data():
    """docstring for create_data"""
    return dict(
        total_topics=randint(1, 100),
        total_comments=randint(1, 100),
        total_ppoints=randint(1, 100),
        total_mpoints=randint(1, 100),
        total_repli=randint(1, 100),
        last_posttime=datetime.datetime.now()
    )


def mapping_sid(id):
    service = {
        0: "cp_test",
        1: "sp_sports",
        2: "sp_news",
        3: "sp_goo",
    }
    dist = id % 4
    return service[dist]

def create_summery():
    summery = {}
    for i in range(4):
        sid = mapping_sid(i)
        record = create_data()
        summery[sid] = record
    print summery
    return summery

create_summery()
exit()

host = "www10284ue.sakura.ne.jp"
r = redis.Redis(host=host)

### delete all data
r.flushall()

### make initial data
datas = []
for i in range(1, 100 + 1):
    record = create_data()
    sid = mapping_sid(i)
    datas.append([sid, record])

### set that
for sid, record in datas:
    r.hmset(sid, record)
    print sid,
    print r.hgetall(sid)
