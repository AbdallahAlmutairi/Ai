"""Simple backend providing placeholder trading features.

This module exposes a small subset of the endpoints described in the
initial design document.  The goal is to provide a working skeleton that
front-end developers can build upon.  Data is stored in memory which means
it will reset whenever the application restarts.  It is **not** meant for
production use but gives an idea of how the API might look.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI(title="AI Stock Bot")


# ---------------------------------------------------------------------------
# In-memory storage used for the demo.  A real implementation would store
# this data in a persistent database with proper authentication.
# ---------------------------------------------------------------------------
watchlist: list[str] = []
risk_profile: str = "moderate"


@app.get("/api/recommendation/{symbol}")
async def recommendation(symbol: str, tf: str = "15m"):
    """Return a placeholder recommendation for a stock symbol.

    Parameters
    ----------
    symbol: str
        The ticker symbol requested by the client.
    tf: str
        Timeframe for the recommendation, default ``"15m"``.
    """

    entry = 100.0
    stop_loss = 95.0
    take_profit = [110.0, 120.0]
    rr_ratio = round((take_profit[0] - entry) / (entry - stop_loss), 2)

    return {
        "symbol": symbol.upper(),
        "timeframe": tf,
        "direction": "long",
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "prob_up": 0.62,
        "rr_ratio": rr_ratio,
        "confidence": "medium",
        "reasoning": [
            "اختراق مقاومة بفوليوم أعلى من المتوسط",
            "RSI يرتفع",
            "غياب أحداث سلبية قريبة",
        ],
        "indicators": {"atr14": 0.28, "rsi14": 56.3, "ema20": 33.22},
        "risk_checks": {"liquidity_ok": True, "event_risk_next_24h": "none"},
        "risk_profile": risk_profile,
    }


@app.get("/api/watchlist")
async def get_watchlist():
    """Return the current watchlist."""

    return {"symbols": watchlist}


@app.post("/api/watchlist/{symbol}")
async def add_to_watchlist(symbol: str):
    """Add a symbol to the watchlist."""

    symbol = symbol.upper()
    if symbol not in watchlist:
        watchlist.append(symbol)
    return {"symbols": watchlist}


@app.delete("/api/watchlist/{symbol}")
async def remove_from_watchlist(symbol: str):
    """Remove a symbol from the watchlist."""

    symbol = symbol.upper()
    try:
        watchlist.remove(symbol)
    except ValueError:
        raise HTTPException(status_code=404, detail="Symbol not in watchlist")
    return {"symbols": watchlist}


@app.get("/api/risk-profile")
async def get_risk_profile():
    """Return the current risk profile."""

    return {"risk_profile": risk_profile}


@app.post("/api/risk-profile/{profile}")
async def set_risk_profile(profile: str):
    """Set the risk profile to one of the allowed values."""

    profile = profile.lower()
    allowed = {"conservative", "moderate", "aggressive"}
    if profile not in allowed:
        raise HTTPException(status_code=400, detail="Invalid profile")

    global risk_profile
    risk_profile = profile
    return {"risk_profile": risk_profile}


app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
async def index():
    """Serve the front-end HTML file."""

    return FileResponse("frontend/index.html")

