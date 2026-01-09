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
ai_trading_app/
│
├── config/ # Django project settings
├── trading_ai/ # Core application
│ ├── services/ # AI logic (data, model, risk, decision)
│ ├── views.py
│ └── urls.py
│
├── templates/ # HTML templates
│ └── index.html
│
├── static/ # Static assets
│ ├── css/style.css
│ └── js/app.js
│
├── manage.py
└── venv/

⚠️ Important Disclaimer

This application is for educational and research purposes only.
It is not financial advice and should not be used for live trading without proper validation, risk management and regulatory compliance.

Markets are unpredictable, and past performance does not guarantee future results.

🧩 Limitations & Future Improvements
Currently trains models in-memory (can be persisted to disk)
Single time resolution (daily data)
No portfolio-level analysis yet
Planned enhancements:
Date range selection
Confidence & risk visualization
Model persistence (disk / Redis)
User accounts & analysis history
Deployment to cloud (PythonAnywhere / VPS)

🤝 Contributing
Pull requests and suggestions are welcome.
Feel free to fork the project and experiment with improvements.

📬 Contact
Built by Tanaka Keith Ndopo
If you’re interested in collaboration, research, or extensions feel free to reach out.
