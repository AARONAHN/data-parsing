import csv
from pymongo import MongoClient
from mongodb import MongoDB
from bson import ObjectId

client = MongoDB()

db = client.session.aaron_db

with open('../data/1490_postback.csv', encoding='utf-8') as csvfile:
    postback_csv = csv.reader(csvfile, delimiter=',')

    head = None

    for i, row in enumerate(postback_csv):
        if i == 0:
            head = row
            print(head)
            continue

        pb_dic = dict(zip(head, row))
        print(pb_dic)

        for k, v in pb_dic.items():
            if k == '_id':
                pb_dic['_id'] = ObjectId(v)

        pb_mongo = db.pb_test2.insert_one(pb_dic)