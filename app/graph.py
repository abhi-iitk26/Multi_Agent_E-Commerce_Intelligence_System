from langgraph.graph import StateGraph
from app.state import AgentState

from app.nodes.research import research_node
from app.nodes.strategy import strategy_node
from app.nodes.content import content_node
from app.nodes.validation import validation_node

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("research", research_node)
    graph.add_node("strategy", strategy_node)
    graph.add_node("content", content_node)

    graph.set_entry_point("research")

    graph.add_edge("research", "strategy")
    graph.add_edge("strategy", "content")

    graph.add_conditional_edges(
        "content",
        validation_node,
        {
            "retry": "research",
            "final": "__end__"
        }
    )

    return graph.compile()
