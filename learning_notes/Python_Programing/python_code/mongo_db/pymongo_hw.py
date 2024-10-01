from pymongo import MongoClient, ASCENDING, DESCENDING
import pymongo
import json


client = MongoClient(host='localhost', port=27017)
db = client['pymongo_test']
collection = db['post']


mydata = json.load(open("data.txt")) 
collection.remove({})

collection.insert_many(mydata)
