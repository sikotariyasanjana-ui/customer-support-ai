"""
Gemini Client (New SDK)
"""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not API_KEY:
    # We will raise a Warning instead of hard failing so the app starts even without a key, 
    # but the chatbot endpoint will warn if the key is missing when called.
    print("⚠️ WARNING: Neither GOOGLE_API_KEY nor GEMINI_API_KEY found in environment variables.")
    client = None
else:
    client = genai.Client(api_key=API_KEY)


def get_llm():
    return client