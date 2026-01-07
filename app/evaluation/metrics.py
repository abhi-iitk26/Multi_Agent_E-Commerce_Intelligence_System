def insight_coverage(insights: dict) -> int:
    return len(insights.get("pain_points", [])) + len(insights.get("positive_signals", []))


def strategy_alignment(insights: dict, strategy: dict) -> float:
    pain = set(insights.get("pain_points", []))
    avoid = set(strategy.get("avoid", []))
    return len(pain & avoid) / max(len(pain), 1)


def content_risk_score(content: str) -> int:
    risky_phrases = ["best ever", "no issues", "perfect", "guaranteed"]
    return sum(p in content.lower() for p in risky_phrases)
