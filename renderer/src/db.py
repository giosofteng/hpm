from pymongo import MongoClient


class DB:
    def __init__(self):
        client = MongoClient()
        db = client['db']
        self.images = db['images']
        self.images.delete_many({})

    def put(self, url):
        self.images.insert_one({'url': url})

    def get(self):
        return self.images.find()
