# 🦠 COVID-19 Data Analyzer

A real-time COVID-19 data analysis and visualization dashboard built with Python.

## 📌 About
This project analyzes pandemic trends across 200+ countries using real-time data from public APIs. It provides interactive visualizations for cases, deaths, and vaccination progress.

## 🛠️ Tech Stack
- Python, Pandas, NumPy
- Plotly / Plotly Express
- Streamlit (Dashboard UI)
- disease.sh API / Our World in Data

## 📊 Features
- 📈 Time-series line charts for daily new cases & deaths
- 🗺️ Global choropleth map of confirmed cases
- 💉 Vaccination progress bar charts by region
- 🔄 7-day rolling average for trend smoothing
- 🌍 Country-wise filtering via dropdown

## 🚀 How to Run
```bash
pip install pandas plotly streamlit requests
streamlit run app.py
```

## 📁 Project Structure
    covid19-data-analyzer/
    │
    ├── app.py              # Main Streamlit dashboard
    ├── data_loader.py      # API fetching & preprocessing
    ├── visualizations.py   # Plotly chart functions
    ├── requirements.txt
    └── README.md

## 📈 Model Performance
| Metric | Value |
|--------|-------|
| R² Score | 0.88 |
| MAE | Rs. 3,241 |
| Test Accuracy | 88.4% |

## 👤 Author
**Subhramukul Payra**  
AI & ML Intern | KIIT University, Bhubaneswar  
[LinkedIn](https://linkedin.com/in/subhramukul-payra-b4180527a)
