from fastapi import FastAPI, Header, HTTPException, Depends, Body
from typing import Optional
from pydantic import BaseModel
import re

# --------------------
# App setup
# --------------------
app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "MY_SECRET_API_KEY_123"

# In-memory storage
conversation_memory = {}

# --------------------
# API Key verification
# --------------------
def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

# --------------------
# Request / Response Models
# --------------------


class ScamResponse(BaseModel):
    is_scam: bool
    details: dict
    summary: str

# --------------------
# Health check (GET)
# --------------------
@app.get("/detect_scam")
def detect_scam_get():
    return {
        "status": "alive",
        "message": "Honeypot endpoint is live. Use POST to analyze messages."
    }

# --------------------
# Main endpoint (POST)
# IMPORTANT: Body(None) prevents 422 error
# --------------------

@app.post("/detect_scam", response_model=ScamResponse)
def detect_scam(
    session_id: Optional[str] = None,
    message: Optional[str] = None,
    api_key: str = Depends(verify_api_key)
):
    session_id = session_id or "default"
    message = message or ""

    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    conversation_memory[session_id].append(message)

    text = message.lower()

    scam_words = ["otp", "urgent", "bank", "upi", "click", "blocked", "pay"]
    is_scam = any(word in text for word in scam_words)

    upi_ids = re.findall(r"\b\w+@\w+\b", message)
    bank_accounts = re.findall(r"\b\d{9,18}\b", message)
    phishing_links = re.findall(r"https?://\S+", message)

    summary = (
        "Agent identified scam intent and is continuing engagement to extract intelligence."
        if is_scam
        else "Agent monitoring conversation."
    )

    return ScamResponse(
        is_scam=is_scam,
        details={
            "upi_ids": upi_ids,
            "bank_accounts": bank_accounts,
            "phishing_links": phishing_links,
            "conversation_length": len(conversation_memory[session_id])
        },
        summary=summary
    )
