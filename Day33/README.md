# Create README file

readme_text = """
# Day 33 - Detecting Unusual Customer Behavior

## Objective

Build an anomaly detection system to identify unusual
customer behavior patterns using sales transaction data.

## What I Built

- Customer-level behavior dataset
- Feature selection for anomaly detection
- Feature standardization
- Isolation Forest anomaly detection
- Normal vs anomalous customer classification
- Anomaly visualization
- Normal vs anomalous behavior comparison
- Business risk analysis

## Features Used

- Total Sales
- Total Quantity
- Total Profit
- Average Discount
- Average Shipping Days
- Number of Orders

## Technique Used

### Isolation Forest

Isolation Forest identifies observations that are
different from the majority of the dataset.

The model labels:

- `1` → Normal
- `-1` → Anomalous

## Process

Sales Data
    ↓
Customer-Level Behavior
    ↓
Feature Selection
    ↓
Standardization
    ↓
Isolation Forest
    ↓
Normal / Anomalous Customers
    ↓
Visualization
    ↓
Business Risk Analysis

## Files

- `day33.ipynb` - Main notebook
- `customer_anomaly_results.csv` - Complete anomaly results
- `anomalous_customers.csv` - Detected anomalous customers
- `behavior_comparison.csv` - Normal vs anomalous comparison
- `customer_anomalies.png` - Anomaly visualization
- `business_risk_analysis.md` - Business risk analysis

## Key Learning

Anomaly detection can help businesses identify unusual
customer behavior and create signals for further analysis.

## Important Note

An anomalous customer is not automatically fraudulent or
suspicious. The model identifies unusual behavior that may
require further investigation.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
"""

with open(
    "README.md",
    "w",
    encoding="utf-8"
) as file:
    file.write(readme_text)

print("README created successfully!")