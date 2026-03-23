# Quick Start Guide for AI Coding Mentor Chatbot

## ⚡ FASTEST WAY TO RUN (3 Steps)

### Step 1: Set Groq API Key
**Windows PowerShell:**
```powershell
$env:GROQ_API_KEY="paste_your_groq_key_here"
```

**Linux/Mac:**
```bash
export GROQ_API_KEY="paste_your_groq_key_here"
```

### Step 2: Install Dependencies & Run Backend
**All Platforms:**
```bash
pip install flask flask-cors groq
python chatbot_backend.py
```

You should see:
```
🚀 Starting AI Coding Mentor Chatbot on http://127.0.0.1:5001
```

### Step 3: Open Frontend
- **Option A:** Double-click `chatbot_frontend.html` in file explorer
- **Option B:** Right-click → Open with → Browser
- **Option C:** Drag file to browser

✅ **Done!** Start typing questions about coding.

---

## 📋 Detailed Setup (With Virtual Environment)

### For Windows:
```powershell
cd "C:\Users\Nithin\Downloads\ai code learning mentor"
python -m venv .venv
.venv\Scripts\activate
pip install flask flask-cors groq
$env:GROQ_API_KEY="your_key_here"
python chatbot_backend.py
```

### For Linux/Mac:
```bash
cd ~/Downloads/ai\ code\ learning\ mentor
python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-cors groq
export GROQ_API_KEY="your_key_here"
python chatbot_backend.py
```

---

## 🔑 Getting Groq API Key

1. Go to https://groq.com
2. Sign up (free)
3. Go to https://console.groq.com/keys
4. Create new API key
5. Copy it and paste in terminal

---

## ❓ Troubleshooting

### "Connection error" in frontend
✅ Make sure backend is running (check terminal shows "Running on http://127.0.0.1:5001")

### "ModuleNotFoundError: No module named 'flask'"
✅ Install dependencies:
```bash
pip install flask flask-cors groq
```

### Backend won't respond to chat
✅ Check GROQ_API_KEY is set:
```powershell
echo $env:GROQ_API_KEY  # Windows
echo $GROQ_API_KEY      # Linux/Mac
```

### Database locked error
✅ Delete `chatbot.db` and restart:
```bash
del chatbot.db
python chatbot_backend.py
```

---

## 🎯 How It Works

```
User: "How do I use lists in Python?"
    ↓
Frontend sends to http://127.0.0.1:5001/chat
    ↓
Backend processes with Groq LLM + previous chat history + learned insights
    ↓
AI extracts learning: "User interested in Python data structures"
    ↓
Insight stored in SQLite hindsight table
    ↓
Response sent back to frontend
    ↓
Next user question uses stored insights for better personalization!
```

---

## 📊 What You Get

- **Smart AI**: Powered by Groq (super fast)
- **Memory**: Every chat saved
- **Learning**: AI remembers your interests and skill level
- **History**: All conversations stored locally
- **No cloud**: All data stays on your computer

---

## 🚀 Ready? Start here:
```bash
pip install flask flask-cors groq
python chatbot_backend.py
```

Then open `chatbot_frontend.html` in your browser! 🎉
