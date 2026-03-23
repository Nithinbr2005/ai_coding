# 🤖 AI Coding Mentor Chatbot

An intelligent chatbot that answers coding questions, remembers past conversations, and improves responses over time using **hindsight learning**.

## 🎯 Features

✅ **Smart AI Responses** — Uses Groq LLM (llama-3.1-8b-instant) for fast, accurate coding help  
✅ **Memory System** — Stores all conversations in SQLite database  
✅ **Hindsight Learning** — Extracts insights from conversations and improves future responses  
✅ **Beautiful Dashboard** — Comprehensive UI with chat, insights, history, and analytics  
✅ **REST API** — Clean endpoints for chat, history, and clearing  
✅ **Persistent Storage** — All data saved locally in `chatbot.db`

## 📁 Project Structure

```
ai code learning mentor/
├── chatbot_backend.py       # Flask backend with Groq integration
├── serve_dashboard.py       # Dashboard web server
├── dashboard.html           # Comprehensive dashboard UI
├── chatbot_frontend.html    # Simple chatbot interface (legacy)
├── start_dashboard.bat      # Windows launcher for dashboard
├── start_dashboard.sh       # Linux/Mac launcher for dashboard
├── CHATBOT_README.md        # This file
└── chatbot.db              # SQLite database (created automatically)
```

## 🗄️ Database Schema

### Table: `chats`
```sql
- id (INTEGER PRIMARY KEY)
- role (TEXT) — 'user' or 'assistant'
- content (TEXT) — message content
- timestamp (DATETIME)
```

### Table: `hindsight`
```sql
- id (INTEGER PRIMARY KEY)
- insight (TEXT) — extracted learning about the user
- timestamp (DATETIME)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API key (get free at https://groq.com)

### Setup (Windows PowerShell)

```powershell
# Navigate to project folder
cd "C:\Users\Nithin\Downloads\ai code learning mentor"

# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate

# Install dependencies
pip install flask flask-cors groq

# Set Groq API key (replace with your actual key)
$env:GROQ_API_KEY="your_groq_api_key_here"

# Run backend
python chatbot_backend.py
```

### Setup (Linux/Mac)

```bash
cd ~/Downloads/ai code learning mentor

python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-cors groq

export GROQ_API_KEY="your_groq_api_key_here"
python chatbot_backend.py
```

## 📖 Running the Project

### Option 1: Dashboard (Recommended)

1. **Start the backend**:
   ```powershell
   python chatbot_backend.py
   ```
   Expected output:
   ```
   🚀 Starting AI Coding Mentor Chatbot on http://127.0.0.1:5001
   ```

2. **Launch the dashboard**:
   - **Windows**: Double-click `start_dashboard.bat`
   - **Linux/Mac**: Run `chmod +x start_dashboard.sh && ./start_dashboard.sh`
   - Or manually: `python serve_dashboard.py`
   - Then visit: `http://127.0.0.1:5001/`

3. **Explore the dashboard**:
   - **Dashboard**: Overview with metrics and quick chat
   - **Chat**: Full-screen chat interface
   - **Insights**: View what AI has learned about you
   - **History**: Browse past conversations
   - **Settings**: Configure API keys and system options

### Option 2: Simple Chat Interface

1. **Start the backend** (same as above)

2. **Open the simple interface**:
   - Double-click `chatbot_frontend.html` in File Explorer
   - Or open in browser: `file:///C:/Users/Nithin/Downloads/ai%20code%20learning%20mentor/chatbot_frontend.html`

3. **Start chatting**:
   - Type a coding question in the input box
   - Click "Send" or press Enter
   - Watch the AI respond with insights

## 🧠 How Hindsight Learning Works

```
User asks question
       ↓
LLM generates response
       ↓
Insight extracted (skill level, interests, mistakes)
       ↓
Insight stored in hindsight table
       ↓
Next conversation uses stored insights as context
       ↓
Response becomes more personalized over time ✨
```

## 📡 API Endpoints

### POST `/chat`
Send a message and get AI response.

**Request:**
```json
{
  "message": "How do I sort a list in Python?"
}
```

**Response:**
```json
{
  "response": "To sort a list in Python...",
  "timestamp": "2024-03-23T10:30:45"
}
```

### GET `/history`
Retrieve all chat history and learned insights.

**Response:**
```json
{
  "chats": [
    {"role": "user", "content": "How do I use loops?"},
    {"role": "assistant", "content": "Loops are used to..."}
  ],
  "insights": [
    "User is beginner in Python",
    "Interested in loops and functions",
    "Struggles with syntax"
  ]
}
```

### POST `/clear`
Delete all chat history and insights.

**Response:**
```json
{
  "status": "ok",
  "message": "All chat history cleared"
}
```

### GET `/health`
Check if backend is running.

**Response:**
```json
{
  "status": "ok",
  "service": "AI Coding Mentor Chatbot"
}
```

## 🎨 Frontend Features

- **Chat Interface** — Clean, modern UI with animations
- **Real-time Messages** — Live response streaming
- **Insights Sidebar** — Shows what AI has learned about you
- **Statistics** — Track messages and insights count
- **Responsive Design** — Works on desktop and mobile
- **Dark/Light Ready** — Adaptive color scheme

## 📊 Dashboard Features

- **Analytics Dashboard** — Real-time metrics and statistics
- **Multi-page Navigation** — Dashboard, Chat, Insights, History, Settings
- **Interactive Chat** — Full-featured chat interface with typing indicators
- **Insights Management** — View and refresh learned insights
- **Chat History** — Browse past conversations with search
- **Settings Panel** — API key management and system controls
- **Responsive Design** — Works on all screen sizes
- **Modern UI** — Beautiful gradients, animations, and icons

## 🔧 Troubleshooting

### Backend won't start
```
Error: GROQ_API_KEY not set
```
**Solution:** Set your API key:
```powershell
$env:GROQ_API_KEY="your_key_here"
python chatbot_backend.py
```

### Frontend can't connect to backend
```
Connection error. Make sure the backend is running on http://127.0.0.1:5001
```
**Solution:** Make sure:
1. Backend is running (`python chatbot_backend.py`)
2. It shows `Running on http://127.0.0.1:5001`
3. Reload the HTML file in browser

### Database errors
```
sqlite3.OperationalError: database is locked
```
**Solution:** 
- Clear old database: delete `chatbot.db`
- Restart backend (it will create new database)

## 📚 Example Conversations

### First message:
```
You: What's the difference between == and is in Python?
AI: The == operator checks for value equality...
   [Insight saved: "User is interested in Python operators"]
```

### Second message (using hindsight):
```
You: How do I check if something is None?
AI: Based on your interest in Python operators...
    You'd use the 'is' operator: if x is None...
    [Insight saved: "User is learning Python best practices"]
```

## 🎯 Hackathon Features

✅ **Persistent Memory** — All conversations saved in SQLite  
✅ **Learning System** — Extracts insights and uses them in future prompts  
✅ **Personalization** — Each user gets increasingly tailored responses  
✅ **Fast Responses** — Powered by Groq's fast inference  
✅ **Clean Architecture** — Separate backend/frontend, easy to extend  

## 🚀 Deployment Notes

For production use:
1. Replace SQLite with PostgreSQL/MongoDB
2. Add user authentication
3. Use `gunicorn` instead of Flask debug server
4. Add rate limiting
5. Enable HTTPS

## 📝 Code Examples

### Custom system prompt with hindsight:
```python
insights_text = "\n".join([f"- {insight}" for insight in insights])
system_prompt = f"""You are an intelligent AI coding mentor...
User insights:
{insights_text}
Remember previous conversations and tailor your responses."""
```

### Extract insights from conversation:
```python
def extract_hindsight(user_message, assistant_response):
    extraction_prompt = f"""
    Based on this conversation, extract ONE key insight...
    User: {user_message}
    Assistant: {assistant_response}
    """
    response = client.messages.create(...)
    save_hindsight(response.content[0].text)
```

## 📞 Support

- **Groq Docs:** https://console.groq.com/docs
- **Flask Docs:** https://flask.palletsprojects.com/
- **SQLite Docs:** https://www.sqlite.org/docs.html

## 📄 License

This project is free to use and modify for hackathon submission.

---

**Built with ❤️ for the Hindsight Hackathon**
