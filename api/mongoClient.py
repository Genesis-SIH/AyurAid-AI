# mongo.py
from pymongo import MongoClient
uri = "mongodb+srv://AyurAid:AyurAid@cluster0.e1veukt.mongodb.net/AyurAid?retryWrites=true&w=majority"

mongoClient = MongoClient(uri)
database = mongoClient['AyurAid']
colChats = database['chats']

