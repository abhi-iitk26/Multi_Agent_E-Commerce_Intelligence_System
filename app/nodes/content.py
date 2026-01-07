from langchain_google_genai import ChatGoogleGenerativeAI
from app.state import AgentState

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.4
)

def content_node(state: AgentState) -> AgentState:
    prompt = f"""
Generate 2–3 sentences of honest, brand-safe marketing content.

Strategy:
{state['strategy']}

Rules:
- No overpromising
- Value-conscious tone
- Avoid risky claims
"""

    content = llm.invoke(prompt).content.strip()

    return {
        **state,
        "content": content
    }
