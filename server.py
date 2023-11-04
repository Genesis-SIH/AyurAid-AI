from flask import Flask, request
import prompt_generator

app = Flask(__name__)

@app.route('/sendprompt', methods=["POST"])
def sendPrompt():
    prompt = request.json['prompt']

    prompt_response = prompt_generator.main(prompt)
    return prompt_response



if __name__ == "__main__":
    app.run(debug=True) 