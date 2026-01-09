import numpy as np

def compute_risk_metrics(
    similar_indices,
    price_series,
    lookback=60,
    horizon=20
):
    """
    Compute win/loss probabilities and drawdown
    based on historical similar patterns.
    """

    prices = price_series.values.flatten()

    returns = []
    drawdowns = []

    for idx in similar_indices:
        entry = idx + lookback
        exit_ = entry + horizon

        if exit_ >= len(prices):
            continue

        entry_price = prices[entry]
        future_prices = prices[entry:exit_]

        max_price = future_prices.max()
        min_price = future_prices.min()

        ret = (max_price - entry_price) / entry_price
        dd = (min_price - entry_price) / entry_price

        returns.append(ret)
        drawdowns.append(dd)

    if not returns:
        return None

    returns = np.array(returns)
    drawdowns = np.array(drawdowns)

    win_prob = np.mean(returns > 0)
    loss_prob = 1 - win_prob

    expected_return = returns.mean()
    expected_drawdown = drawdowns.mean()

    confidence = win_prob * (1 - abs(expected_drawdown))

    return {
        "win_probability": float(win_prob),
        "loss_probability": float(loss_prob),
        "expected_return": float(expected_return),
        "expected_drawdown": float(expected_drawdown),
        "confidence": float(confidence)
    }
