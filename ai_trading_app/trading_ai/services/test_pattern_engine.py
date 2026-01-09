from data_loader import fetch_stock_data
from preprocessing import preprocess_data
from model import build_lstm_model, train_model
from pattern_engine import find_similar_patterns
from holding_period import estimate_holding_period

if __name__ == "__main__":
    df = fetch_stock_data("AAPL", "2019-01-01", "2023-01-01")
    X, y, scaler = preprocess_data(df)

    model = build_lstm_model((X.shape[1], X.shape[2]))
    train_model(model, X, y)

    similar_outcomes, similar_indices = find_similar_patterns(X, y)

    holding_days = estimate_holding_period(
        similar_indices,
        df["Close"]
    )

    print("Similar patterns found:", len(similar_indices))
    print("Estimated holding period (days):", holding_days)
    print("Average outcome:", similar_outcomes.mean())
