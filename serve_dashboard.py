from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'dashboard.html')

@app.route('/dashboard.html')
def dashboard():
    return send_from_directory('.', 'dashboard.html')

@app.route('/chatbot_frontend.html')
def legacy_chat():
    return send_from_directory('.', 'chatbot_frontend.html')

if __name__ == '__main__':
    print("🚀 Dashboard server starting...")
    print("📊 Visit: http://127.0.0.1:5001/")
    print("💬 Legacy chat: http://127.0.0.1:5001/chatbot_frontend.html")
    app.run(host='127.0.0.1', port=5001, debug=False)