from fastapi import FastAPI
from pydantic import BaseModel
import re
# Simple in-memory conversation store
conversation_memory = {}


#Create the API app(The door)
app=FastAPI(title="Agentic Honey-Pot API")

#Request schema
class ScamRequest(BaseModel):
    session_id: str
    message: str
#Request schema
class ScamResponse(BaseModel):
    is_scam:bool
    details:dict
    summary:str

@app.post("/detect-scam", response_model=ScamResponse)
def detect_scam(request: ScamRequest):
    session_id = request.session_id
    message = request.message

    # Initialize memory
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    # Store message
    conversation_memory[session_id].append(message)

    text = message.lower()

    # Scam detection
    is_scam = any(
        word in text
        for word in ["otp", "urgent", "bank", "upi", "click", "blocked", "pay"]
    )

    # Regex extraction
    upi_pattern = r"\b[\w.-]+@[\w.-]+\b"
    bank_pattern = r"\b\d{9,18}\b"
    link_pattern = r"https?://[^\s]+"

    upi_ids = re.findall(upi_pattern, message)
    bank_accounts = re.findall(bank_pattern, message)
    phishing_links = re.findall(link_pattern, message)

    # Agentic summary (persona-based)
    if is_scam:
        summary = "Agent identified scam intent and is continuing engagement to extract intelligence."
    else:
        summary = "Agent monitoring conversation."

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

        