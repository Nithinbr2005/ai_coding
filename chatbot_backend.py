import os
import json
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, will use system env vars

app = Flask(__name__)
CORS(app)

# Initialize Groq client
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
client = Groq(api_key=GROQ_API_KEY)

DB_NAME = 'chatbot.db'

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create chats table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create hindsight table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hindsight (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            insight TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()

def get_chat_history(limit=20):
    """Fetch recent chat history from database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT role, content FROM chats ORDER BY id DESC LIMIT ? ', (limit,))
    rows = cursor.fetchall()
    conn.close()
    
    # Reverse to get chronological order
    history = [{'role': role, 'content': content} for role, content in reversed(rows)]
    return history

def get_hindsight_insights():
    """Fetch all stored hindsight insights"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT insight FROM hindsight ORDER BY id DESC LIMIT 10')
    rows = cursor.fetchall()
    conn.close()
    
    insights = [row[0] for row in rows]
    return insights

def save_chat(role, content):
    """Save chat message to database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO chats (role, content) VALUES (?, ?)', (role, content))
    conn.commit()
    conn.close()

def save_hindsight(insight):
    """Save hindsight insight to database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO hindsight (insight) VALUES (?)', (insight,))
    conn.commit()
    conn.close()

def extract_hindsight(user_message, assistant_response):
    """Use LLM to extract insights from conversation"""
    try:
        extraction_prompt = f"""
Based on this conversation, extract ONE key insight about the user's coding knowledge, interests, or mistakes.
Keep it concise (1 sentence max).

User: {user_message}
Assistant: {assistant_response}

Insight:"""
        
        message = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": extraction_prompt}]
        )
        
        insight = message.choices[0].message.content.strip()
        if insight:
            save_hindsight(insight)
        return insight
    except Exception as e:
        print(f"Error extracting hindsight: {e}")
        return None

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        if not GROQ_API_KEY:
            return jsonify({'error': 'GROQ_API_KEY environment variable not set'}), 500
        
        # Save user message
        save_chat('user', user_message)
        
        # Get chat history and hindsight insights
        history = get_chat_history(limit=10)
        insights = get_hindsight_insights()
        
        # Build system prompt with hindsight
        insights_text = "\n".join([f"- {insight}" for insight in insights]) if insights else "No previous insights yet."
        
        system_prompt = f"""You are an intelligent AI coding mentor. Help users learn programming in a simple and structured way.

User insights:
{insights_text}

Remember previous conversations and tailor your responses based on what you've learned about the user."""
        
        # Prepare messages for LLM
        messages = [
            {"role": "user", "content": system_prompt}
        ]
        
        # Add chat history
        for msg in history:
            messages.append({"role": msg['role'], "content": msg['content']})
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        # Get response from Groq
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        assistant_message = response.choices[0].message.content
        
        # Save assistant response
        save_chat('assistant', assistant_message)
        
        # Extract and save hindsight
        extract_hindsight(user_message, assistant_message)
        
        return jsonify({
            'response': assistant_message,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/clear', methods=['POST'])
def clear_chat():
    """Clear all chat history and hindsight"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM chats')
        cursor.execute('DELETE FROM hindsight')
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'ok', 'message': 'All chat history cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/history', methods=['GET'])
def get_history():
    """Get full chat history"""
    try:
        history = get_chat_history(limit=50)
        insights = get_hindsight_insights()
        
        return jsonify({
            'chats': history,
            'insights': insights
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'AI Coding Mentor Chatbot'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    print(f"🚀 Starting AI Coding Mentor Chatbot on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
