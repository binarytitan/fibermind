from flask import Flask, request, jsonify
from openai import ChatCompletion

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot Server is running!"

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    chat_model = "gpt-3.5-turbo"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message},
    ]
    response = ChatCompletion.create(model=chat_model, messages=messages)
    return jsonify(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    app.run(debug=True)
