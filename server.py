from flask import Flask, request, jsonify
import mongo
from mongo import myCollection


# using time module
import time

app = Flask(__name__)


@app.route('/chatbot/ask', methods=['POST'])
def askChatbot():
    prompt = request.json['prompt']
    chatId = request.json["chatId"]

    ts = time.time()
    userMessage = {
        "id": ts,
        "type": "user",
        "timestamp": ts,
        "message": prompt,
        "data":None,
    }

    answer = "hello usr"

    tsBot = time.time()
    botMessage = {
        "id": tsBot,
        "type": "bot",
        "timestamp": tsBot,
        "message": answer,
        "data":None,

    }


    thisCollection = myCollection.find_one({"id": chatId})

    if thisCollection is not None:
        temp = []
        temp = thisCollection["chats"]
        temp.append(userMessage)
        temp.append(botMessage)

        myCollection.update_one({"id":chatId},{"$set":{"chats":temp}})
        print("Saved Success")
    else:
        temp = []
        temp.append(userMessage)
        temp.append(botMessage)

        myCollection.insert_one({"id":chatId,"chats":temp})
        print("Saved Sucess")
        
    return jsonify({'answer': answer})


@app.route('/chatbot/get', methods=['POST'])
def getChatsRoute():
    chatId = request.json["chatId"]

    thisCollection = myCollection.find_one({"id": chatId})

    if thisCollection is not None:
        print(thisCollection)
        return jsonify({'chats': thisCollection["chats"],"success":True})
    else:
        return jsonify({'chats': None,"success":False})

   

@app.route('/blog/ask', methods=['POST'])
def askBlogAi():
    prompt = request.json['prompt']
    # # type = request.json['type']
    # # timestamp = request.json['timestamp']
    # # id = request.json['id']
    # # data = request.json['data']

    # answer = prompt_generator.final_result(prompt)


# @app.route('/blog/ask', methods=['GET'])
# def getChats(collectionId, chatId):
#     thisCollection = myCollection.find_one({"id": "collectionId"})

#     if thisCollection is not None:
#         for chat in thisCollection.get("chats", []):
#             if chatId in chat:
#                 return chat[chatId]

#     return None


# @app.route('/exercise/ask', methods=['POST'])
# def addBlock():
#     content = request.json
#     return jsonify({'answer': dummyText})

if __name__ == "__main__":
    app.run(debug=True) 