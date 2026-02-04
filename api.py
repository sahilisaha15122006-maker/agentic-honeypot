from fastapi import FastAPI, Header, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import re


app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "MY_SECRET_API_KEY_123"


conversation_memory = {}

# ---------------- AUTH ----------------
def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

# ---------------- MODELS ----------------
class ScamRequest(BaseModel):
    session_id: Optional[str] = "default"
    message: Optional[str] = "health check"

class ScamResponse(BaseModel):
    is_scam: bool
    details: dict
    summary: str

# ---------------- HEALTH CHECK ----------------
@app.get("/detect_scam")
def health():
    return {
        "status": "alive",
        "message": "Honeypot endpoint is live"
    }

# ---------------- MAIN ENDPOINT ----------------
@app.post("/detect_scam", response_model=ScamResponse)
def detect_scam(
    request: Optional[ScamRequest] = None,
    api_key: str = Depends(verify_api_key)
):
    # Handle EMPTY body (important)
    if request is None:
        request = ScamRequest()

    session_id = request.session_id or "default"
    message = request.message or "health check"

    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    conversation_memory[session_id].append(message)

    text = message.lower()
    scam_words = ["otp", "urgent", "bank", "upi", "blocked", "pay", "click"]
    is_scam = any(word in text for word in scam_words)

    upi_ids = re.findall(r"\b\w+@\w+\b", message)
    bank_accounts = re.findall(r"\b\d{9,18}\b", message)
    phishing_links = re.findall(r"https?://\S+", message)

    summary = (
        "Agent identified scam intent and is engaging attacker."
        if is_scam
        else "Agent monitoring conversation."
    )

    return ScamResponse(
        is_scam=is_scam,
        details={
            "upi_ids": upi_ids,
            "bank_accounts": bank_accounts,
            "phishing_links": phishing_links,
            "conversation_length": len(conversation_memory[session_id]),
        },
        summary=summary,
    )
