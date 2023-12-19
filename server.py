from flask import Flask, request, jsonify
import prompt_generator
import mongo


# using time module
import time

app = Flask(__name__)


@app.route('/chatbot/ask', methods=['POST'])
def askChatbot():
    prompt = request.json['prompt']

    ts = time.time()
    userMessage = {
        "id": ts,
        "type": "user",
        "timestamp": ts,
        "message": prompt,
        "data":None,
    }

    answer = prompt_generator.final_result(prompt)

    tsBot = time.time()

    botMessage = {
        "id": tsBot,
        "type": "bot",
        "timestamp": tsBot,
        "message": answer,
        "data":None,
    }

    # mongo.saveChat(userMessage)
    # mongo.saveChat(botMessage)

    return jsonify({'answer': answer})


@app.route('/blog/ask', methods=['POST'])
def askBlogAi():
    prompt = request.json['prompt']
    # type = request.json['type']
    # timestamp = request.json['timestamp']
    # id = request.json['id']
    # data = request.json['data']

    answer = prompt_generator.final_result(prompt)


    return jsonify({'answer': answer})



# @app.route('/exercise/ask', methods=['POST'])
# def addBlock():
#     content = request.json
#     return jsonify({'answer': dummyText})

if __name__ == "__main__":
    app.run(debug=True) 