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

📁 Project Structure (STANDARD PRACTICE)
ecommerce_agentic_ai/
│
├── main.py
├── graph.py
├── state.py
│
├── agents/
│   ├── research_agent.py
│   ├── strategy_agent.py
│   ├── content_agent.py
│
├── tools/
│   └── search.py
│
├── evaluation/
│   └── metrics.py
│
├── requirements.txt
└── README.md