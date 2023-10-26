from pymongo import MongoClient


class DB:
    def __init__(self):
        client = MongoClient('mongo')  # ! DEBUG
        db = client['db']
        self.images = db['images']
        self.empty()

    def put(self, url):
        if self.images.count_documents({}) > 1000:
            print("DB EMPTIED")  # ! DEBUG
            self.empty()
        self.images.insert_one({'url': url})

    def get(self):
        return self.images.find()

    def empty(self):
        self.images.delete_many({})
