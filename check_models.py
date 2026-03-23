#!/usr/bin/env python3
"""
Check available Groq models
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

try:
    models = client.models.list()
    print("Available models:")
    for model in models.data:
        print(f"  - {model.id}")
except Exception as e:
    print(f"Error: {e}")
    print("\nCommon working models to try:")
    print("  - llama3-8b-8192")
    print("  - llama3-70b-8192")
    print("  - mixtral-8x7b-32768")
    print("  - gemma-7b-it")
    print("  - llama2-70b-4096")
    print("  - codellama-34b-instruct")
    print("\nOr check: https://console.groq.com/docs/models")