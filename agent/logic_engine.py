import networkx as nx

class LogicEngine:
    def __init__(self):
        # We use a Directed Graph to track the flow of the argument
        self.graph = nx.DiGraph()
        self.claims = {}

    def add_claim(self, claim_id: str, text: str, parent_id: str = None):
        """Adds a new premise to the map."""
        self.graph.add_node(claim_id, label=text, type="premise")
        if parent_id and parent_id in self.graph:
            self.graph.add_edge(parent_id, claim_id)
        
        self.claims[claim_id] = text
        return {"id": claim_id, "label": text, "type": "premise", "parentId": parent_id}

    def detect_aporia(self, new_claim_text: str):
        """
        Simple keyword-based or logic-path detection. 
        In production, the Cartographer (LLM) will trigger this.
        """
        # Logic: If the user previously said 'A' and now says 'Not A'
        # This will be refined by the Cartographer agent's reasoning.
        pass

    def get_map_state(self):
        """Returns the current graph for the D3.js frontend."""
        return nx.node_link_data(self.graph)
