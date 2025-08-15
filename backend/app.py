from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="AI Stock Bot")

@app.get("/api/recommendation/{symbol}")
async def recommendation(symbol: str):
    """Return a placeholder recommendation for a stock symbol."""
    return {
        "symbol": symbol.upper(),
        "action": "buy",
        "confidence": 0.75,
        "entry": 100.0,
        "stop": 95.0,
        "targets": [110.0, 120.0],
        "rationale": ["breakout", "volume spike"]
    }

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def index():
    return FileResponse("frontend/index.html")
