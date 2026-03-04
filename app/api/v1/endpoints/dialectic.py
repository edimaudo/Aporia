from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.philosopher import get_philosopher_config
from app.services.cartographer import Cartographer
import json

router = APIRouter()
cartographer = Cartographer()

@router.websocket("/dialectic")
async def socratic_session(websocket: WebSocket):
    await websocket.accept()
    
    # In a real build, you'd initialize the Gemini Live client here
    try:
        while True:
            # Listen for incoming audio/data
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # If user speaks, philosopher responds (Audio)
            # Simultaneously, cartographer updates the map (Data)
            if message.get("type") == "user_input":
                # Background analysis for the map
                node = cartographer.analyze_logic(message["text"])
                await websocket.send_json({"type": "logic_update", "node": node})
                
    except WebSocketDisconnect:
        print("Dialectic terminated.")
