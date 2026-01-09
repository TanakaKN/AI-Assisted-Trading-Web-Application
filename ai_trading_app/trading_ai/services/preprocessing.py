import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df, feature_col="Close", lookback=60):
    """
    Convert price series into scaled time-series windows.
    """
    data = df[[feature_col]].values

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    X, y = [], []

    for i in range(lookback, len(scaled_data)):
        X.append(scaled_data[i - lookback:i, 0])
        y.append(scaled_data[i, 0])

    X, y = np.array(X), np.array(y)

    # LSTM expects 3D input
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    return X, y, scaler
