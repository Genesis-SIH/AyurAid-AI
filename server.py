from flask import Flask, request, jsonify
from mongo import myCollection
import prompt_generator
from flask_cors import CORS, cross_origin

# using time module
import time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/util/wakeup', methods=['GET'])
def wakeupServer():
    return jsonify({'message': 'Hello User'})

@app.route('/chatbot/ask', methods=['POST'])
@cross_origin(["http://localhost:4000","https://ayur-aid-web.vercel.app"])
def askChatbot():
    prompt = request.json['prompt']
    chatId = request.json["chatId"]

    ts = time.time()
    userMessage = {
        "id": ts,
        "type": "user",
        "timestamp": ts,
        "text": prompt,
        "data":None,
    }

    answer = prompt_generator.final_result(prompt)
    
    
    tsBot = time.time()
    botMessage = {
        "id": tsBot,
        "type": "bot",
        "timestamp": tsBot,
        "text": answer,
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
@cross_origin(["http://localhost:4000","https://ayur-aid-web.vercel.app"])
def getChatsRoute():
    chatId = request.json["chatId"]

    thisCollection = myCollection.find_one({"id": chatId})

    if thisCollection is not None:
        print(thisCollection)
        return jsonify({'chats': thisCollection["chats"],"success":True})
    else:
        return jsonify({'chats': None,"success":False})

   

@app.route('/blog/ask', methods=['POST'])
@cross_origin(["http://localhost:4000","https://ayur-aid-web.vercel.app"])
def askBlogAi():
    prompt = request.json['prompt']

    answer = prompt_generator.final_result(prompt)
    
    return jsonify({'answer': answer})



if __name__ == "__main__":
    app.run(host='0.0.0.0') 
