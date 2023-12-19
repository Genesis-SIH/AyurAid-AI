from pymongo import MongoClient


uri = "mongodb+srv://AyurAid:AyurAid@cluster0.e1veukt.mongodb.net/AyurAid?retryWrites=true&w=majority"


myClient = MongoClient(uri)
myDb = myClient["AyurAid"]
myCollection = myDb["chatbot"]


def saveChat(data):
    thisChat = myCollection.find_one({"id": data["id"]})
    if thisChat is None:
        tempChats = []
        tempChats.append(data)
        myCollection.insert_one({"id": data["id"], "chats": tempChats})
    else:
        tempChats = []
        for chat in thisChat["chats"]:
            tempChats.append(chat)

        tempChats.append(data)
        myCollection.update_one({"id": data["id"]}, {"$set": data})
    