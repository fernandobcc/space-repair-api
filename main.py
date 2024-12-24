import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

DAMAGED_SYSTEM = "engines"

SYSTEM_CODES = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05",
}


@app.get("/status", response_class=JSONResponse)
async def get_status():
    """
    First call: Return the damaged system as JSON.
    """
    return {"damaged_system": DAMAGED_SYSTEM}


@app.get("/repair-bay", response_class=HTMLResponse)
async def get_repair_bay():
    """
    Second call: Generate an HTML page with the system code.
    """
    system_code = SYSTEM_CODES.get(DAMAGED_SYSTEM, "UNKNOWN")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{system_code}</div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.post("/teapot")
async def post_teapot(response: Response):
    """
    Third call: Return HTTP status 418 (I'm a teapot).
    """
    response.status_code = 418
    return {"message": "I'm a teapot"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
