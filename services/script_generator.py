import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent?key="
    + GEMINI_KEY
)


def create_script(topic):

    prompt = f"""
Create an engaging YouTube Shorts script about:

{topic}

Requirements:
- 45–60 seconds
- Strong hook
- Easy English
- Viral style
- Call to action
"""

    response = requests.post(
        URL,
        json={
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }
    )

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
0

