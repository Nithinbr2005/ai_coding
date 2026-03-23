#!/usr/bin/env python3
"""
Environment Setup and Chatbot Launcher
Automatically loads .env file and starts the chatbot backend
"""

import os
import sys
import subprocess
from pathlib import Path

print("=" * 60)
print("🤖 AI CODING MENTOR CHATBOT - LAUNCHER")
print("=" * 60)

# Check if .env exists
env_file = Path('.env')
if not env_file.exists():
    print("\n❌ ERROR: .env file not found!")
    print("Please create .env with your GROQ_API_KEY")
    print("\nExample:")
    print("  GROQ_API_KEY=your_key_here")
    print("  PORT=5001")
    sys.exit(1)

# Load .env
print("\n[1] Loading configuration from .env...")
from dotenv import load_dotenv
load_dotenv()

groq_key = os.getenv('GROQ_API_KEY')
port = os.getenv('PORT', '5001')

if not groq_key:
    print("❌ GROQ_API_KEY not found in .env!")
    sys.exit(1)

print(f"✅ GROQ_API_KEY: {groq_key[:10]}...")
print(f"✅ PORT: {port}")

# Check dependencies
print("\n[2] Checking dependencies...")
try:
    import flask
    import flask_cors
    import groq
    print("✅ All dependencies installed")
except ImportError as e:
    print(f"❌ Missing dependency: {e}")
    print("Run: pip install flask flask-cors groq python-dotenv")
    sys.exit(1)

# Check database
print("\n[3] Initializing database...")
import sqlite3
conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY,
        role TEXT,
        content TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS hindsight (
        id INTEGER PRIMARY KEY,
        insight TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()
conn.close()
print("✅ Database ready")

# Start server
print("\n" + "=" * 60)
print("🚀 Starting AI Coding Mentor Chatbot")
print("=" * 60)
print(f"\n📍 Backend: http://127.0.0.1:{port}")
print("📍 Frontend: Open chatbot_frontend.html in browser")
print("\nPress CTRL+C to stop server")
print("=" * 60 + "\n")

os.system('python chatbot_backend.py')
