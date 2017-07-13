from pymongo import MongoClient


class MongoDB():
    def __init__(self):
        self.session = MongoClient(host='localhost', port=27017)

