from flask import Flask, request, jsonify


app = Flask(__name__)

dummyText  = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris lobortis convallis erat et hendrerit. Nulla non metus eu velit sollicitudin consequat. Etiam egestas nisl ac nulla elementum, ac ullamcorper leo pretium. Phasellus id pharetra neque. Integer malesuada bibendum mattis. Vestibulum bibendum ligula non convallis volutpat. Nulla at porttitor purus. Duis a eros hendrerit, vehicula nisi sit amet, mattis urna. Aliquam ultrices leo ut enim scelerisque, elementum consequat dui imperdiet. Phasellus eu gravida erat. Curabitur volutpat tortor ut ligula rhoncus bibendum sit amet at velit.
"""

@app.route('/chatbot/ask', methods=['POST'])
def initChain():
    content = request.json
    return jsonify({'answer': dummyText})


@app.route('/exercise/ask', methods=['POST'])
def addBlock():
    content = request.json
    return jsonify({'answer': dummyText})

if __name__ == "__main__":
    app.run(debug=False) 