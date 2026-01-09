from data_loader import fetch_stock_data
from preprocessing import preprocess_data
from model import build_lstm_model, train_model, predict

if __name__ == "__main__":
    df = fetch_stock_data("AAPL", "2019-01-01", "2023-01-01")
    X, y, scaler = preprocess_data(df)

    model = build_lstm_model((X.shape[1], X.shape[2]))
    history = train_model(model, X, y)

    preds = predict(model, X)

    print("Predictions shape:", preds.shape)
    print("Last prediction (scaled):", preds[-1][0])
