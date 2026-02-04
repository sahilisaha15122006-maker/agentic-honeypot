# Agentic HoneyPot API

An AI-powered security API that detects scam and phishing messages using rule-based analysis and conversational memory.

## Problem
Scam and phishing messages cause financial loss and data theft. Users often fail to identify malicious intent in time.

## Solution
This project provides a REST API that analyzes incoming messages and identifies scam patterns such as urgency, payment requests, and phishing keywords.

## Features
- Scam and phishing detection
- Session-based conversation memory
- API key–protected endpoint
- FastAPI with Swagger documentation

## API Endpoint
**POST** `/detect_scam`

### Authentication

This API uses an API key for authentication.

**Demo API key (for judges/testing):**
x-api-key: MY_SECRET_API_KEY_123

**Headers**
- `x-api-key`: API authentication key

**Request Body**
```json
{
  "session_id": "demo1",
  "message": "Your bank account is blocked. Pay by UPI now."
}
# agentic-honeypot
