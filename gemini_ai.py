import google.generativeai as genai
import os
from google import generativeai as genai

#Set your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model=genai.Generative.Model("gemini-pro")

def analyze_login(log_dta):
    prompt=f"""
You are a cybersecurity AI.

analyze this login attempt and classify it as:
-normal
-suspicious
-malicious

Also explain WHY and suggest an action.

login data:
Username:{log_data['username']}
Password:{log_data['password']}
Time:{log_data['time']}
"""

    response=model.generate_content(prompt)
    return response.text