@echo off
REM AI Coding Mentor Chatbot Launcher for Windows

echo.
echo ================================
echo AI Coding Mentor Chatbot
echo ================================
echo.

REM Check if .env file exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please create .env file with GROQ_API_KEY
    pause
    exit /b 1
)

REM Load .env and start server
echo Loading configuration from .env...
for /f "tokens=1,2 delims==" %%a in (.env) do (
    if "%%a"=="GROQ_API_KEY" set GROQ_API_KEY=%%b
    if "%%a"=="PORT" set PORT=%%b
)

if not defined GROQ_API_KEY (
    echo ERROR: GROQ_API_KEY not found in .env!
    pause
    exit /b 1
)

echo GROQ_API_KEY: %GROQ_API_KEY:~0,10%...
echo PORT: %PORT%
echo.
echo Starting Flask backend...
echo.

python chatbot_backend.py

pause
