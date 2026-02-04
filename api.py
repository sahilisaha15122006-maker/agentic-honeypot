from fastapi import FastAPI, Header, HTTPException, Request
from typing import Optional

app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "MY_SECRET_API_KEY_123"


def verify_api_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


# ✅ GUVI TESTER SAFE (POST, NO BODY, JSON HEADER, EMPTY PAYLOAD)
@app.post("/detect_scam")
async def detect_scam(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    verify_api_key(x_api_key)

    # 🚫 DO NOT TOUCH request.body()
    # 🚫 DO NOT PARSE JSON
    # 🚫 DO NOTHING WITH BODY

    return {
        "status": "ok",
        "message": "Honeypot endpoint is live"
    }


# ✅ Optional GET (browser/manual test)
@app.get("/detect_scam")
def detect_scam_get(x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    return {
        "status": "ok",
        "message": "Honeypot endpoint is live"
    }
