import json
from langchain_google_genai import ChatGoogleGenerativeAI
from app.state import AgentState

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

def research_node(state: AgentState) -> AgentState:
    context = "\n".join(state["raw_inputs"])

    prompt = f"""
You are a customer insights analyst.

Extract ONLY valid JSON with:
- pain_points: list[str]
- positive_signals: list[str]
- sentiment_score: float (0–1)

Data:
{context}
"""

    response = llm.invoke(prompt).content
    insights = json.loads(response)

    return {
        **state,
        "insights": insights,
        "confidence": insights["sentiment_score"]
    }
