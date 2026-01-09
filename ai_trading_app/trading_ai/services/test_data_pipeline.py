from data_loader import fetch_stock_data
from preprocessing import preprocess_data

if __name__ == "__main__":
    df = fetch_stock_data("AAPL", "2019-01-01", "2023-01-01")
    X, y, scaler = preprocess_data(df)

    print("DataFrame shape:", df.shape)
    print("X shape:", X.shape)
    print("y shape:", y.shape)
