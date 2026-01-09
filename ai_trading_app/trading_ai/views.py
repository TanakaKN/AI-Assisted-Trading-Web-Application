from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from trading_ai.services.data_loader import fetch_stock_data
from trading_ai.services.preprocessing import preprocess_data
from trading_ai.services.model import build_lstm_model, train_model, predict
from trading_ai.services.pattern_engine import find_similar_patterns
from trading_ai.services.holding_period import estimate_holding_period
from trading_ai.services.risk_engine import compute_risk_metrics
from trading_ai.services.decision_engine import make_decision


# -----------------------------
# SIMPLE IN-MEMORY MODEL CACHE
# -----------------------------
MODEL_CACHE = {}

STOCK_CHOICES = [
    "AAPL", "MSFT", "GOOGL", "AMZN",
    "TSLA", "META", "NVDA", "JPM", "NFLX"
]


def home(request):
    return render(request, "index.html", {"stocks": STOCK_CHOICES})


@csrf_exempt
def analyze_stock(request):
    print(">>> ANALYZE ENDPOINT HIT <<<")
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)

    ticker = request.POST.get("ticker")

    if ticker not in STOCK_CHOICES:
        return JsonResponse({"error": "Invalid ticker selected"}, status=400)

    # -----------------------------
    # DATA PIPELINE
    # -----------------------------
    df = fetch_stock_data(ticker, "2019-01-01", "2023-01-01")
    X, y, scaler = preprocess_data(df)

    # -----------------------------
    # MODEL CACHE LOGIC
    # -----------------------------
    if ticker in MODEL_CACHE:
        model = MODEL_CACHE[ticker]
    else:
        model = build_lstm_model((X.shape[1], X.shape[2]))
        train_model(model, X, y)
        MODEL_CACHE[ticker] = model

    predictions = predict(model, X)
    last_prediction = predictions[-1][0]
    current_price = df["Close"].values[-1]

    # -----------------------------
    # PATTERN + RISK
    # -----------------------------
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
        last_prediction=last_prediction,
        current_price=current_price,
        risk_metrics=risk_metrics,
        avg_pattern_outcome=avg_pattern_outcome,
        holding_period=holding_period
    )

    return JsonResponse({
        "ticker": ticker,
        "decision": decision,
        "cached": ticker in MODEL_CACHE
    })
