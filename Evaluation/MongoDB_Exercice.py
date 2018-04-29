#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:19:26 2018

@author: hot
"""
import pymongo
from pymongo import MongoClient
import pprint
import csv

csvfile = open('/user/hot/DRIO_Data/OUAP_4314/OUAP-4314/Mongo/data/ks-projects-201801-sample.csv','r')
data = csv.DictReader(csvfile)
client = MongoClient()
db = client.data_test
header= ["ID","name","category","main_category","currency","deadline","goal","launched","pledged","state","backers","country","usd pledged","usd_pledged_real"]


    
for each in data:
    row={}
    for field in header:
        row[field]=each[field]
    db.segment.insert(row)
    
cursor = db.segment.find().sort("pledged",pymongo.DESCENDING)
for post in cursor.limit(5):
    pprint.pprint(post)
    