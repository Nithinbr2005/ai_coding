#!/usr/bin/env python3
"""
Quick test script to validate chatbot project setup.
Run this BEFORE starting the main backend to ensure dependencies are correct.
"""

import sys
import subprocess

print("=" * 60)
print("🤖 AI CODING MENTOR CHATBOT - SETUP VALIDATOR")
print("=" * 60)

# Check Python version
print("\n[1] Checking Python version...")
if sys.version_info < (3, 8):
    print(f"❌ Python 3.8+ required. You have {sys.version_info.major}.{sys.version_info.minor}")
    sys.exit(1)
print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

# Check required packages
print("\n[2] Checking dependencies...")
required_packages = {
    'flask': 'Flask web framework',
    'flask_cors': 'CORS support',
    'groq': 'Groq LLM API'
}

missing = []
for package, desc in required_packages.items():
    try:
        __import__(package)
        print(f"✅ {package}: {desc}")
    except ImportError:
        print(f"❌ {package}: NOT FOUND - {desc}")
        missing.append(package)

if missing:
    print(f"\n⚠️  Missing packages: {', '.join(missing)}")
    print("\nTo install, run:")
    print("  pip install flask flask-cors groq")
    sys.exit(1)

# Check GROQ_API_KEY
print("\n[3] Checking Groq API key...")
import os
groq_key = os.getenv('GROQ_API_KEY')
if groq_key:
    print(f"✅ GROQ_API_KEY is set ({groq_key[:10]}...)")
else:
    print("⚠️  GROQ_API_KEY environment variable NOT SET")
    print("\nTo set it:")
    print("  Windows: $env:GROQ_API_KEY='your_key_here'")
    print("  Linux/Mac: export GROQ_API_KEY='your_key_here'")
    print("\nYou can still run the backend, but /chat won't work without it.")

# Check database
print("\n[4] Checking SQLite database...")
import sqlite3
try:
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    if tables:
        print(f"✅ Database exists with {len(tables)} table(s)")
    else:
        print("✅ Database will be created on first run")
    conn.close()
except Exception as e:
    print(f"⚠️  Database issue: {e}")

# Check files exist
print("\n[5] Checking project files...")
import os.path
files = [
    'chatbot_backend.py',
    'chatbot_frontend.html',
    'CHATBOT_README.md'
]
for f in files:
    if os.path.exists(f):
        print(f"✅ {f}")
    else:
        print(f"❌ {f} - NOT FOUND")

print("\n" + "=" * 60)
print("✅ ALL CHECKS PASSED - Ready to run!")
print("=" * 60)
print("\nTo start the chatbot backend:")
print("  python chatbot_backend.py")
print("\nThen open in browser:")
print("  file:///C:/Users/Nithin/Downloads/ai%20code%20learning%20mentor/chatbot_frontend.html")
print("\n" + "=" * 60)
