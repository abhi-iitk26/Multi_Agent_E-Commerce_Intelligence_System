from app.state import AgentState

CONFIDENCE_THRESHOLD = 0.6

def validation_node(state: AgentState) -> str:
    if state["confidence"] < CONFIDENCE_THRESHOLD:
        return "retry"
    return "final"
