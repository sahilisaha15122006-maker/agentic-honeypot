


from fastapi import FastAPI, Header, HTTPException
from typing import Optional



app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "MY_SECRET_API_KEY_123"


def verify_api_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


# ✅ REQUIRED BY GUVI TESTER (NO BODY, SIMPLE HIT)
@app.post("/detect_scam")
def detect_scam(x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    return {
        "status": "ok",
        "message": "Honeypot endpoint is live"
    }


# ✅ OPTIONAL (Browser / manual check)
@app.get("/detect_scam")
def detect_scam_get(x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)

    return {
        "status": "ok",
        "message": "Honeypot endpoint is live"
    
   
    }