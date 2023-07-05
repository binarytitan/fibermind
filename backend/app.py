from flask import Flask, request, jsonify
from openai import OpenAI, GPT3Completion

app = Flask(__name__)
openai = OpenAI("your-openai-api-key")

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if 'messages' not in data:
        return jsonify({'error': 'No messages in request'}), 400
    prompt = '\n'.join([f"{message['sender']}: {message['text']}" for message in data['messages']])
    response = openai.complete(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=60
    )
    return jsonify({'message': response['choices'][0]['text'].strip()})

if __name__ == '__main__':
    app.run(port=5000)
