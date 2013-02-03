#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import csv
import dbm
import gdbm

def parse_line(row):
    """docstring for parse_line"""
    fields = [
        #row[1],
        row[2],
        row[6],
        row[7],
        row[8],
    ]
    return ','.join(fields)

#f = open('./27OSAKA.CSV', 'r')
f = open('./KEN_ALL.CSV', 'r')
reader = csv.reader(f)

db = dbm.open('zip_local', 'c')

for row in reader:
    if not unicode(row[8], 'UTF-8') == u'以下に掲載がない場合':
        zip_code = row[2]
        address = parse_line(row)
        db[zip_code] = address

for k in db.keys():
    print db[k]
