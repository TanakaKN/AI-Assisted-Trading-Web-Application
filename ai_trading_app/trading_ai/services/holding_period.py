import numpy as np

def estimate_holding_period(similar_indices, price_series, lookback=60):
    """
    Estimate holding period based on time to local peak after similar patterns.
    """
    holding_periods = []

    prices = price_series.values.flatten()

    for idx in similar_indices:
        start = idx + lookback
        if start + 30 >= len(prices):
            continue

        future_window = prices[start:start + 30]
        peak_day = future_window.argmax()

        holding_periods.append(peak_day)

    if not holding_periods:
        return None

    return int(np.mean(holding_periods))
