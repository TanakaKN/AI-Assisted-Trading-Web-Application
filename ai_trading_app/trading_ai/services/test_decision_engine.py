from data_loader import fetch_stock_data
from preprocessing import preprocess_data
from model import build_lstm_model, train_model, predict
from pattern_engine import find_similar_patterns
from holding_period import estimate_holding_period
from risk_engine import compute_risk_metrics
from decision_engine import make_decision

if __name__ == "__main__":
    df = fetch_stock_data("AAPL", "2019-01-01", "2023-01-01")
    X, y, scaler = preprocess_data(df)

    model = build_lstm_model((X.shape[1], X.shape[2]))
    train_model(model, X, y)

    preds = predict(model, X)
    last_pred = preds[-1][0]
    current_price = df["Close"].values[-1]

    similar_outcomes, similar_indices = find_similar_patterns(X, y)
    avg_pattern_outcome = similar_outcomes.mean()

    holding_period = estimate_holding_period(
        similar_indices,
        df["Close"]
    )

    risk_metrics = compute_risk_metrics(
        similar_indices,
        df["Close"]
    )

    decision = make_decision(
        last_prediction=last_pred,
        current_price=current_price,
        risk_metrics=risk_metrics,
        avg_pattern_outcome=avg_pattern_outcome,
        holding_period=holding_period
    )

    print(decision)
