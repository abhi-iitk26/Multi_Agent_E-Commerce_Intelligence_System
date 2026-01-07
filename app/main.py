import os
from dotenv import load_dotenv
from app.graph import build_graph
from app.tools.serper import serper_search
from app.evaluation.metrics import (
    insight_coverage,
    strategy_alignment,
    content_risk_score
)

load_dotenv()

def main():
    external_data = serper_search("budget smartphone complaints india")

    input_state = {
        "raw_inputs": external_data + [
            "Good camera but battery drains fast",
            "Value for money phone but heating issue"
        ],
        "insights": None,
        "strategy": None,
        "content": None,
        "confidence": 0.0
    }

    app = build_graph()
    result = app.invoke(input_state)

    print("\n=== FINAL OUTPUT ===")
    print("INSIGHTS:", result["insights"])
    print("\nSTRATEGY:", result["strategy"])
    print("\nCONTENT:", result["content"])

    print("\n=== EVALUATION ===")
    print("Insight coverage:", insight_coverage(result["insights"]))
    print("Strategy alignment:", strategy_alignment(result["insights"], result["strategy"]))
    print("Content risk score:", content_risk_score(result["content"]))


if __name__ == "__main__":
    main()
