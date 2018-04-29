#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:44:56 2018

@author: hot
"""

import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.test_database

collection = db.test_collection

post = {
    "url" : "string",
    "domaine": "String",
    "title" : "String",
    "type": "String",
    "room_number":123456,
    "phone_number":1020,
    "bed_room_number":301,
    "bath_room_number":302,
    "construction_year":303,
    "area" : 4040,
    "storey" : 7077,
    "total_storey" : 2300,
    "description" : "nice",
    "ges" : "ges",
    "energy" : "over 9000",
    "location":"sevran",
    "local_id":"89898650",
    "images":["avc","abc"]
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

print(db.collection_names(include_system_collections=False))