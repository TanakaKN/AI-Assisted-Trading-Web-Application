def make_decision(
    last_prediction,
    current_price,
    risk_metrics,
    avg_pattern_outcome,
    holding_period
):
    """
    Combine model prediction, pattern memory, and risk metrics
    to produce a BUY / SELL / HOLD decision.
    """

    explanation = []

    if risk_metrics is None:
        return {
            "action": "HOLD",
            "confidence": 0.0,
            "explanation": ["Insufficient historical data for risk evaluation."]
        }

    confidence = risk_metrics["confidence"]

    # Decision rules
    if (
        last_prediction > current_price and
        risk_metrics["win_probability"] > 0.6 and
        avg_pattern_outcome > 0
    ):
        action = "BUY"
        explanation.append("Upward price movement predicted.")
        explanation.append("Majority of similar historical patterns resulted in gains.")

    elif (
        last_prediction < current_price and
        risk_metrics["loss_probability"] > 0.6 and
        avg_pattern_outcome < 0
    ):
        action = "SELL"
        explanation.append("Downward price movement predicted.")
        explanation.append("Similar historical patterns show downside risk.")

    else:
        action = "HOLD"
        explanation.append("Signals are mixed or risk is elevated.")

    explanation.append(
        f"Win probability: {risk_metrics['win_probability']:.2f}, "
        f"Expected drawdown: {risk_metrics['expected_drawdown']:.2f}"
    )

    if holding_period:
        explanation.append(
            f"Typical holding period based on similar patterns: {holding_period} days."
        )

    return {
        "action": action,
        "confidence": round(confidence, 2),
        "explanation": explanation
    }
