from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key=os.getenv("AIzaSyCi0mbXfp0uEBZpK7n-YnqR9tXT0tyXSM0"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('prompt')
    
    # Start chat or continue existing conversation
    if 'chat' not in request.json:
        chat = model.start_chat(history=[])
    else:
        chat = request.json['chat']
    
    # Get response from Gemini
    response = chat.send_message(user_input)
    
    return jsonify({
        "response": response.text,
        "chat": chat
    })

if __name__ == '__main__':
    app.run(debug=True)

