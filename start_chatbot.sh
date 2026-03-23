#!/bin/bash
#
# AI Coding Mentor Chatbot Launcher for Linux/Mac
#

echo ""
echo "======================================"
echo "AI Coding Mentor Chatbot"
echo "======================================"
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ ERROR: .env file not found!"
    echo "Please create .env with your GROQ_API_KEY"
    echo ""
    echo "Example:"
    echo "  GROQ_API_KEY=your_key_here"
    echo "  PORT=5001"
    exit 1
fi

echo "[1] Loading configuration from .env..."

# Load .env
export $(grep -v '^#' .env | xargs)

if [ -z "$GROQ_API_KEY" ]; then
    echo "❌ ERROR: GROQ_API_KEY not found in .env!"
    exit 1
fi

echo "✅ GROQ_API_KEY: ${GROQ_API_KEY:0:10}..."
echo "✅ PORT: ${PORT:-5001}"

echo ""
echo "[2] Checking dependencies..."
python3 -c "import flask, flask_cors, groq" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Missing dependencies!"
    echo "Run: pip install flask flask-cors groq python-dotenv"
    exit 1
fi
echo "✅ All dependencies installed"

echo ""
echo "======================================"
echo "🚀 Starting AI Coding Mentor Chatbot"
echo "======================================"
echo ""
echo "📍 Backend: http://127.0.0.1:${PORT:-5001}"
echo "📍 Frontend: Open chatbot_frontend.html in browser"
echo ""
echo "Press CTRL+C to stop server"
echo "======================================"
echo ""

# Start server
python3 chatbot_backend.py
