# Create Day 34 README

readme = """# Day 34 - Designing Executive-Level Customer Dashboards

## Overview

Day 34 focuses on designing an executive-level customer analytics dashboard for business decision-making.

The dashboard combines customer segmentation, business KPIs, sales trends, profit performance, and customer activity risk into one business-friendly view.

## Objectives

- Create an executive customer analytics dashboard
- Visualize customer segmentation
- Display important business KPIs
- Analyze sales and profit performance
- Visualize monthly sales trends
- Identify customer activity risk
- Document dashboard storytelling decisions

## Dashboard Components

### KPI Cards

- Total Customers
- Total Sales
- Total Profit
- Total Orders

### Customer Segmentation

The dashboard compares:

- High-Value Customers
- Regular Customers

### Profit Analysis

Average profit is compared across customer segments.

### Sales Trend

Monthly sales are visualized to understand changes in business performance over time.

### Customer Activity Risk

Customers are grouped into Low, Medium, and High activity-risk categories based on days since their latest order.

This is a recency-based activity-risk proxy and is not a confirmed churn prediction.

## Files

- `day34.ipynb` - Dashboard notebook
- `executive_kpi_cards.png` - KPI cards
- `customer_segmentation.png` - Customer segmentation chart
- `segment_sales_profit_comparison.png` - Segment sales and profit comparison
- `customer_risk_overview.png` - Customer behavior risk chart
- `monthly_sales_trend.png` - Monthly sales trend
- `customer_activity_risk.png` - Activity-risk chart
- `executive_customer_dashboard.png` - Complete executive dashboard
- `business_insight_summary.md` - Business insights
- `dashboard_storytelling.md` - Dashboard storytelling decisions

## Business Value

The dashboard provides a single view of customer and business performance.

It helps decision-makers quickly understand:

- Customer distribution
- Customer value
- Profit differences
- Sales trends
- Customer activity risk

## Learning Outcome

This task demonstrates how data analysis results can be transformed into an executive-friendly dashboard that communicates business insights clearly.
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print("README created successfully!")
print("Saved as: README.md")