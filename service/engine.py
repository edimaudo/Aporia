import networkx as nx

class LogicEngine:
    def __init__(self):
        # We use a Directed Graph to show how one idea leads to another
        self.graph = nx.DiGraph()

    def add_claim(self, claim_id: str, text: str, parent_id: str = None):
        """Adds a node to the mental map and links it to its premise."""
        
        # Default status is 'premise'
        node_status = "premise"
        
        # Add the node with its metadata
        self.graph.add_node(claim_id, label=text, status=node_status)
        
        # If this claim follows from a previous one, draw the edge
        if parent_id and self.graph.has_node(parent_id):
            self.graph.add_edge(parent_id, claim_id)
            
        return {
            "id": claim_id,
            "label": text,
            "status": node_status,
            "parent": parent_id
        }

    def check_for_aporia(self, claim_id: str):
        """
        Logic to detect if this node contradicts previous nodes.
        In the hackathon version, this could be a call back to Gemini.
        """
        return False
