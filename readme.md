# Space Repair API

This API simulates a distress signal from a spaceship, allowing a repair robot to identify and fix a damaged system. The API is built using FastAPI.

## Endpoints

1. **GET /status**: Returns the damaged system.
2. **GET /repair-bay**: Provides an HTML page with the repair system code.
3. **POST /teapot**: Responds with HTTP status 418 ("I'm a teapot").

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/space-repair-api.git


2. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```