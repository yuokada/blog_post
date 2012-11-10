#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from sqlalchemy import (create_engine, MetaData, Table, Column, Integer,
                        String, ForeignKey, Float, DateTime, event)
from sqlalchemy.orm import sessionmaker, mapper, relationship
from sqlalchemy.ext.horizontal_shard import ShardedSession
from sqlalchemy.sql import operators ,visitors

import datetime

echo = True
db1 = create_engine('sqlite://',echo=echo, pool_threadlocal=True)
db2 = create_engine('sqlite://',echo=echo)
db3 = create_engine('sqlite://',echo=echo)
db4 = create_engine('sqlite://',echo=echo)

create_session = sessionmaker(class_=ShardedSession)
create_session.configure (shards ={
        'north_america':db1,
        'asia':db2,
        'europe':db3,
        'south_america':db4,
})

meta = MetaData()

ids = Table('ids', meta,
            Column('next_id', Integer, nullable=False)
)

def id_generate():
     c = db1.connect()
     nextid = c.execute(ids.select(for_update=True)).scalar()
     c.excute(dis.update(values={ids.c.nextid : ids.c.nextid + 1}))
     return nextid


wheather_locations = Table('weather_locations', meta,
                           Column('id', Integer, primary_key=True, default=id_generate),
                           Column('continent', String(30), nullable=False),
                           Column('city', String(30), nullable=False))


wheather_reports = Table('wheather_reports', meta,
                         Column('id', Integer, primary_key=True),
                         Column('location_id',Integer, ForeignKey('weather_locations.id')),
                         Column('temperature', Float,),
                         Column('report_time', DateTime, default=datetime.datetime))

for db in (db1, db2, db3, db4):
     meta.drop_all(db)
     meta.create_all(db)

# establish initial "id" in db1
db1.execute(ids.insert(), nextid=1)

shard_lookup = {
     'North_America':'north_america',
     'Asia': 'asia',
     'Europe':'europe',
     'South_America': 'south_america',
     }



                                  
                                  

if __name__ == '__main__':
    print id_generate()
