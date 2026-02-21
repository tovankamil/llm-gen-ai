import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_AI_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [{"text": "You are an expert in software engineering specially python django and only answer backend app. Please acknowledge this."}]
        },
        {
            "role": "model", 
            "parts": [{"text": "Understood. I will act as an expert in software engineering with specialization in Python and Django backend development. I will focus exclusively on backend-related topics and provide guidance on server-side architecture, database design, API development, and Django best practices."}]
        }
    ]
)

response = chat.send_message("How to become master software engineer")
print(response.text)