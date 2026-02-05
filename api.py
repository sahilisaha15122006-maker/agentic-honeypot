from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "MY_SECRET_API_KEY_123"


def verify_api_key(x_api_key: str | None):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


@app.post("/detect_scam")
async def detect_scam(
    request: Request,
    x_api_key: str | None = Header(None)
):
    verify_api_key(x_api_key)

    try:
        body = await request.json()
    except Exception:
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "reply": "Invalid JSON body"
            }
        )

    # Extract message text safely
    message_text = (
        body.get("message", {})
        .get("text", "")
        .lower()
    )

    # Simple honeypot-style response
    if "bank" in message_text or "blocked" in message_text:
        reply = "Why is my account being suspended?"
    else:
        reply = "Can you explain this message?"

    return {
        "status": "success",
        "reply": reply
    }


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Agentic Honeypot API is running"
    }
