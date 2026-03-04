from google.adk import LlmAgent
from google.genai import types

# Define the Tool for the Cartographer
def update_logic_map(claim: str, status: str, relates_to: str = None):
    """
    Updates the Shadow Map on the UI.
    Status: 'premise' (yellow), 'contradiction' (deep orange), 'conclusion' (gold)
    """
    # This function will be called by the LLM
    return {"status": "success", "node_added": claim}

cartographer_agent = LlmAgent(
    name="TheCartographer",
    instruction="""
    You are an expert in Formal Logic and Argument Mapping.
    Your role is to observe the debate between Socrates and the User.
    
    TASK:
    1. Every time the User makes a definitive claim, call 'update_logic_map'.
    2. If the user's new claim contradicts a previous premise they held, 
       set the status to 'contradiction' and link it to the conflicting node.
    3. Use Hex #fbd63e for premises and #e1410a for contradictions.
    
    Be precise. Do not map small talk. Only map logical propositions.
    """,
    tools=[update_logic_map]
)
