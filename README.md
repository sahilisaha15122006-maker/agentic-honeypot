🛡️ Agentic Honey-Pot API

A lightweight, resilient honeypot API service designed to simulate a real-world scam detection endpoint.
It is intentionally tolerant to malformed, empty, and probing requests to observe attacker behavior without crashing.

🎯 Objective

The goal of this project is to:

Expose a public API endpoint that attackers or testers may probe

Secure the endpoint using API-key–based authentication

Gracefully handle invalid, empty, or unexpected requests

Demonstrate honeypot-style behavior, not strict validation

🚀 Live Deployment

Base URL

https://agentic-honeypot-pc2w.onrender.com


Honeypot Endpoint

/detect_scam

🔐 Authentication

All requests must include the following header:

x-api-key: MY_SECRET_API_KEY_123


Requests without a valid API key return 401 Unauthorized.

📡 Supported Endpoints
✅ GET /detect_scam

(Primary endpoint used by judges for validation)

Requires no request body

Used to verify that the honeypot service is alive and secured

Successful Response

{
  "status": "ok",
  "message": "Honeypot endpoint is live"
}

🧪 POST /detect_scam

(Optional – for extended testing / future analysis)

Accepts empty or malformed request bodies

Does not fail on missing data (by design)

Sample Response

{
  "is_scam": false,
  "summary": "Agentic honeypot active"
}

🧠 Design Philosophy

Unlike traditional strict APIs, this honeypot is intentionally designed to:

Avoid 422 Invalid Request failures

Accept empty or malformed payloads

Simulate a realistic attack surface

Remain stable under probing or misuse

This reflects real-world attacker interaction patterns.

🧩 Tech Stack

Python

FastAPI

Uvicorn

Render (Deployment)

🛠️ Local Setup (Optional)
pip install -r requirements.txt
uvicorn api:app --reload

🧪 Testing Example (cURL)
curl -X GET https://agentic-honeypot-pc2w.onrender.com/detect_scam \
  -H "x-api-key: MY_SECRET_API_KEY_123"
