# mongo.py
from pymongo import MongoClient

class MongoDB:
    def __init__(self, host='localhost', port=27017, db_name='test', collection_name='test'):
        self.client = MongoClient(host, port)
        self.db = self.client["test"]
        self.collection = self.db["test"]

    def close_connection(self):
        self.client.close()

