from flask import Flask, request, jsonify
import prompt_generator

app = Flask(__name__)


@app.route('/chatbot/ask', methods=['POST'])
def askChatbot():
    prompt = request.json['prompt']
    # type = request.json['type']
    # timestamp = request.json['timestamp']
    # id = request.json['id']
    # data = request.json['data']

    answer = prompt_generator.final_result(prompt)


    return jsonify({'answer': answer})


@app.route('/blog/ask', methods=['POST'])
def askChatbot():
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
    app.run(host='0.0.0.0') 