# 🛡️ Agentic Honey-Pot API

An Agentic Honeypot REST API that simulates a real user when receiving scam or fraudulent messages.  
The system safely engages scammers, avoids revealing detection, and returns structured JSON responses compatible with automated evaluation.

---

## 🚀 Live Deployment

**Base URL**
https://agentic-honeypot-pc2w.onrender.com
**Swagger Documentation**
https://agentic-honeypot-pc2w.onrender.com/docs


> Note: This is a POST-based API.  
> It is not intended to be accessed directly via a browser URL bar.

---

## 🔐 Authentication
All requests require an API key.
x-api-key: MY_SECRET_API_KEY_123

---

## 📌 Core Endpoint

### POST `/detect_scam`

Accepts an incoming message event and returns an agentic honeypot reply.

---

## 📥 Sample Request

```json
{
  "sessionId": "test-session-id",
  "message": {
    "sender": "scammer",
    "text": "Your bank account will be blocked today. Verify immediately.",
    "timestamp": 1769776085000
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}
{
  "status": "success",
  "reply": "Why is my account being suspended?"
}
