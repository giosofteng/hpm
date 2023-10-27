import os
from pymongo import MongoClient


class DB:
    def __init__(self):
        host = os.environ.get('MONGO_URI', 'mongo')
        client = MongoClient(host)
        db = client['db']
        self.images = db['images']
        self.empty()

    def put(self, url):
        if self.images.count_documents({}) > 1000:
            self.empty()
            # print("DB EMPTIED")  # ! DEBUG
        self.images.insert_one({'url': url})

    def get(self):
        return self.images.find()

    def empty(self):
        self.images.delete_many({})
