from typing import TypedDict, List, Optional, Dict

class AgentState(TypedDict):
    raw_inputs: List[str]
    insights: Optional[Dict]
    strategy: Optional[Dict]
    content: Optional[str]
    confidence: float

