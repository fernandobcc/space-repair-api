import uvicorn
import random
from fastapi import FastAPI, Response
from http import HTTPStatus
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

DAMAGED_SYSTEM = [
    "navigation",
    "communications",
    "life_support",
    "engines",
    "deflector_shield",
]

SYSTEM_CODES = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05",
}

damaged_system = random.choice(DAMAGED_SYSTEM)


@app.get("/status", response_class=JSONResponse)
async def get_status():
    """
    First call: Return the damaged system as JSON.
    """
    return {"damaged_system": damaged_system}


@app.get("/repair-bay", response_class=HTMLResponse)
async def get_repair_bay():
    """
    Second call: Generate an HTML page with the system code.
    """
    system_code = SYSTEM_CODES.get(damaged_system, "UNKNOWN")
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
async def teapot(response: Response):
    response.status_code = HTTPStatus.IM_A_TEAPOT
    return {"message": "I'm a teapot"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
