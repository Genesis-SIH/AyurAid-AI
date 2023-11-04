from flask import Flask, request, jsonify
import prompt_generator

app = Flask(__name__)


initDone = False

@app.route('/init')
def initChain():
    global initDone
    prompt_generator.main()
    initDone = True
    return "Init success"

@app.route('/ask', methods=["POST"])
def ask():
    global initDone
    prompt = request.json['prompt']

    if initDone == False:
        initChain()

    response = prompt_generator.ask(prompt)
    return jsonify({"data":response[1]}) 
  

if __name__ == "__main__":
    app.run(debug=True) 