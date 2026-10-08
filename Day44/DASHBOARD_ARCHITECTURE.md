# Customer Intelligence Dashboard Architecture

## Overview

The Day 44 Customer Intelligence Dashboard is an interactive Streamlit
application designed to provide business insights from customer and sales
data.

## Architecture

Customer CSV Data
        ↓
Data Loading
        ↓
Data Cleaning and Preparation
        ↓
Interactive Filters
        ↓
KPI Calculations
        ↓
Customer Segmentation
        ↓
Churn-Risk Analysis
        ↓
Revenue and Profit Visualizations
        ↓
Interactive Business Dashboard

## Main Components

### 1. Data Source

The dashboard uses the cleaned customer sales dataset:

`cleaned_dataset.csv`

Users can also upload their own compatible CSV file through the dashboard.

### 2. KPI Layer

The dashboard calculates:

- Total Revenue
- Total Profit
- Total Customers
- Total Orders

### 3. Customer Segmentation

Customer segmentation results from Day 30 are displayed to understand
different customer groups.

### 4. Churn-Risk Analysis

Customer risk results from Day 41 are displayed using:

- Low Risk
- Medium Risk
- High Risk

### 5. Interactive Filters

Users can filter the dashboard by:

- Customer
- Product Category

### 6. Visualizations

The dashboard provides:

- Customer segment distribution
- Churn-risk distribution
- Monthly revenue trend
- Profit by category

### 7. Technology Stack

- Python
- Streamlit
- Pandas
- Data Visualization
- CSV datasets

## Business Purpose

The dashboard transforms customer analytics results into an interactive
business intelligence system.

It helps users monitor business performance, understand customer groups,
identify churn-risk customers, and analyze revenue and profit trends.