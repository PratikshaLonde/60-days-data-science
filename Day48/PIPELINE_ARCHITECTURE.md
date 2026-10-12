# Day 48: Customer Intelligence Data Pipeline

## 1. Project Overview
The data pipeline prepares customer and sales data for analysis in the Customer Intelligence Platform.

## 2. Input Dataset
- Source: `../cleaned_dataset.csv`
- Original rows: 51,290
- Original columns: 23

## 3. Pipeline Workflow
1. Load the source dataset.
2. Inspect dataset dimensions, data types, missing values, and duplicate rows.
3. Remove duplicate records.
4. Convert order and shipping dates to datetime format.
5. Convert important numeric columns to numeric types.
6. Create additional analytical features.
7. Validate the processed dataset.
8. Save the output as `cleaned_customer_data.csv`.

## 4. Feature Engineering
Five additional features were created:
- `order_month`
- `order_day`
- `order_day_of_week`
- `sales_category`
- `profit_status`

## 5. Validation Results
- Original rows: 51,290
- Processed rows: 51,290
- Rows removed: 0
- Missing values after processing: 0
- Duplicate rows after processing: 0
- Final columns: 28

## 6. Output
The processed dataset is saved in the Day48 folder as `cleaned_customer_data.csv`.

## 7. Conclusion
A reusable preprocessing function was implemented and tested. The resulting dataset is ready for further customer and sales analysis.
