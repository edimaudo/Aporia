import os
import json
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from google import genai
from google.genai import types

# Import our Socratic logic
from agent.philosopher import get_philosopher_config
from agent.cartographer import cartographer_agent
from agent.logic_engine import LogicEngine

app = FastAPI(title="Aporia: The Digital Lyceum")
engine = LogicEngine()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options={'api_version': 'v1alpha'}
)

@app.websocket("/ws/socratic-live")
async def aporia_session(websocket: WebSocket):
    await websocket.accept()
    
    # Initialize the Socratic Live Session
    config = get_philosopher_config()
    
    try:
        async with client.aio.live.connect(model=config.model, config=config) as session:
            
            async def handle_audio_out():
                """Sends AI voice back to the user."""
                async for response in session.receive():
                    if response.data:
                        await websocket.send_bytes(response.data)
                    
                    # Whenever Gemini generates text, we pass it to the Cartographer
                    if response.text:
                        await process_logic_mapping(response.text, websocket)

            async def handle_audio_in():
                """Receives user voice and pipes to Gemini."""
                async for message in websocket.iter_bytes():
                    await session.send(input=message, end_of_turn=True)

            # Run both streams concurrently
            await asyncio.gather(handle_audio_in(), handle_audio_out())

    except WebSocketDisconnect:
        print("🏛️ Dialectic concluded.")

async def process_logic_mapping(transcript: str, websocket: WebSocket):
    """
    Background Task: The Cartographer Agent analyzes the transcript
    and sends JSON nodes to the D3.js frontend.
    """
    # Use the Cartographer to find logical claims
    # This is a non-blocking background call
    logic_update = await cartographer_agent.analyze(transcript)
    
    if logic_update:
        # Update the local NetworkX engine
        node_data = engine.add_claim(
            claim_id=logic_update['id'],
            text=logic_update['claim'],
            parent_id=logic_update.get('parentId')
        )
        
        # Push to Frontend for D3.js rendering
        await websocket.send_text(json.dumps({
            "type": "logic_node",
            "node": node_data
        }))
