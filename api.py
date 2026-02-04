from fastapi import FastAPI, Header, HTTPException, Body
from typing import Optional



app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "MY_SECRET_API_KEY_123"


def verify_api_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


@app.post("/detect_scam")
def detect_scam(
    x_api_key: Optional[str] = Header(None),
    body: Optional[dict] = Body(None)  # Accepts optional body explicitly
):
    verify_api_key(x_api_key)

    return {
        "is_scam": False,
        "details": {
            "conversation_length": 0
        },
        "summary": "Agent active and monitoring"
   
    }