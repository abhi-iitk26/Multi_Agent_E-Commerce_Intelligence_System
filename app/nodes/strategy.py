import json
from langchain_google_genai import ChatGoogleGenerativeAI
from app.state import AgentState

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)

def strategy_node(state: AgentState) -> AgentState:
    prompt = f"""
Given customer insights below, return ONLY JSON with:
- target_segment
- demand_strategy
- highlight: list[str]
- avoid: list[str]

Insights:
{state['insights']}
"""

    response = llm.invoke(prompt).content
    strategy = json.loads(response)

    return {
        **state,
        "strategy": strategy
    }
