from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints import dialectic

app = FastAPI(title="Aporia")

# Connect the Socratic WebSocket logic
app.include_router(dialectic.router, prefix="/api/v1")

# Mount the frontend. 
# This serves index.html at '/', and debate.html at '/debate.html'
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
