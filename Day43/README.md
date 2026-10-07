# Day 43/60 — Turning Customer Intelligence Model into an API

## Phase: Data Science Deployment

Day 43 focuses on deploying a customer churn-risk prediction model as a
Flask API.

## Project Objective

The goal is to convert the customer risk prediction model developed earlier
into an API that can receive customer information and return a real-time
risk prediction.

## Model Used

Random Forest Classifier

The model uses the following customer features:

- Total Sales
- Total Profit
- Total Quantity
- Number of Orders
- Average Discount
- Average Shipping Days

## API Endpoints

### Home Endpoint

```text
GET /