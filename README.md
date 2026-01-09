# 📈 AI-Assisted Trading Web Application

An AI-powered trading assistant built with **Python, Django, and Neural Networks** that analyzes historical stock data, identifies similar past market patterns, evaluates risk, and provides **BUY / SELL / HOLD** recommendations with confidence and holding-period guidance.

---

## 🚀 Features

- 📊 Fetches real market data from **Yahoo Finance**
- 🧠 Uses **LSTM neural networks** for time-series price modeling
- 🔍 Identifies **historically similar market patterns**
- ⚖️ Computes **win/loss probabilities and expected drawdown**
- 🕒 Estimates **optimal holding period** based on past behavior
- ✅ Produces **explainable trading decisions**
- 🌐 Simple **Django web interface**
- ⏳ Loading spinner and progress feedback
- ⚡ **Model caching per ticker** for faster repeat analysis

---

## 🧠 How It Works (High-Level)

1. User selects a stock ticker from a dropdown list  
2. Historical price data is fetched from Yahoo Finance  
3. Data is cleaned, scaled, and converted into time-series windows  
4. An LSTM model learns price dynamics  
5. The current market pattern is compared to similar historical patterns  
6. Risk metrics (win probability, drawdown) are calculated  
7. All signals are combined into a **BUY / SELL / HOLD** decision  
8. Results are displayed with confidence and explanation  

---

## 🏗️ Technology Stack

- **Backend:** Python, Django  
- **Machine Learning:** TensorFlow / Keras, NumPy, Pandas, Scikit-learn  
- **Data Source:** Yahoo Finance (`yfinance`)  
- **Frontend:** HTML, CSS, JavaScript (no frameworks)  

---

## 📁 Project Structure

