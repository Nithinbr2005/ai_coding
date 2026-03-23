#!/usr/bin/env python3
"""
Quick test script to verify the updated Groq API integration
"""

import os
import requests
from dotenv import load_dotenv

# Load environment
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

if not GROQ_API_KEY:
    print("❌ GROQ_API_KEY not found in .env")
    exit(1)

print("✅ API Key loaded")
print("✅ Testing chatbot backend...")

# Test health endpoint
try:
    response = requests.get("http://127.0.0.1:5001/health")
    if response.status_code == 200:
        print("✅ Health check passed")
    else:
        print(f"❌ Health check failed: {response.status_code}")
        exit(1)
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(1)

# Test chat endpoint
try:
    response = requests.post("http://127.0.0.1:5001/chat", json={"message": "Hello, give me a simple Python question"})
    if response.status_code == 200:
        data = response.json()
        print("✅ Chat endpoint working")
        print(f"Response: {data['response'][:100]}...")
    else:
        print(f"❌ Chat endpoint failed: {response.status_code} - {response.text}")
        exit(1)
except Exception as e:
    print(f"❌ Chat test failed: {e}")
    exit(1)

print("\n🎉 All tests passed! Chatbot is ready.")
print("Open chatbot_frontend.html in your browser to start chatting!")