# Day 36/60 — Forecasting Customer Growth Trends

## 📌 Overview

Day 36 focuses on Time Series Analytics and forecasting future customer growth using historical business data.

The goal was to analyze historical customer activity, identify trends and weekly patterns, build a baseline forecasting model, and predict customer activity for the next 30 days.

---

## 🎯 Objectives

- Load historical customer data
- Convert transaction data into a daily time series
- Visualize customer growth trends
- Calculate a 7-day rolling average
- Analyze monthly customer activity
- Identify weekly patterns
- Build a baseline forecasting model
- Forecast customer activity for the next 30 days
- Document forecasting observations and risks

---

## 📊 Data Preparation

The cleaned sales dataset from the previous days was used.

Customer activity was aggregated by date using the number of unique customers.

Missing dates were added to create a continuous daily time series.

---

## 📈 Trend Analysis

The following analyses were performed:

### Daily Customer Trend

The daily number of unique customers was visualized to understand changes in customer activity over time.

### 7-Day Rolling Average

A 7-day rolling average was calculated to smooth daily fluctuations and identify the broader customer activity trend.

### Monthly Customer Growth

Monthly unique customer counts were calculated to observe longer-term changes.

### Weekly Seasonality

Average customer activity was calculated for each day of the week to identify possible weekly patterns.

---

## 🔮 Forecasting Model

A simple baseline forecasting approach was used.

The average number of customers from the most recent 7 days was calculated and used as the predicted customer activity for each day of the next 30 days.

This model provides a simple benchmark for future forecasting improvements.

---

## 📁 Output Files

```text
Day36/
│
├── day36.ipynb
├── customer_growth_30_day_forecast.csv
├── forecast_summary.csv
└── README.md