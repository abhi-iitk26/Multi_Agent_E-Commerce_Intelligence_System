## Multi-Agent E-Commerce Intelligence System

Production-grade agentic AI system that converts unstructured customer signals into:
- Structured insights
- Demand-shaping strategies
- Personalized content

### Tech
- LangGraph (agent orchestration)
- Gemini 1.5 (reasoning)
- Serper API (external signals)

### Key Features
- Multi-agent reasoning
- Self-healing retries
- Explicit state modeling
- Evaluation metrics
- Docker-ready architecture

# 📁 Project Structure (Standard Practice)

```text
ecommerce_agentic_ai/
│
├── main.py                  # Application entry point
├── graph.py                 # Agent workflow / orchestration logic
├── state.py                 # Shared state management across agents
│
├── agents/
│   ├── research_agent.py    # Market & product research agent
│   ├── strategy_agent.py    # Decision-making & strategy agent
│   └── content_agent.py     # Content generation agent
│
├── tools/
│   └── search.py            # External search / API tools
│
├── evaluation/
│   └── metrics.py           # Model & recommendation evaluation metrics
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
