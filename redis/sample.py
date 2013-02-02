#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import redis

host = "www10284ue.sakura.ne.jp"
r = redis.Redis(host=host)

r.set('foo', '100')
print r.get('foo')

#r.delete('pre_recent')


for i in range(20):
    r.lpush('recent', i)

###
print r.mget(['recent'])
current = r.lrange('recent', 0, -1)
current.extend(r.lrange('pre_recent',0,-1) )
print current

r.rename('recent', 'pre_recent')

print r.lrange('pre_recent', 0, -1)
