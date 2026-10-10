# Day 46: Production Monitoring Report

## 1. Project Overview
The objective of Day 46 is to improve the reliability of the Customer Intelligence Platform using logging, data validation, request tracking, and exception handling.

## 2. Technologies Used
- Python
- Pandas
- Python Logging
- pathlib
- Git and GitHub

## 3. Dataset Details
- Dataset: `cleaned_dataset.csv`
- Total rows: 51,290
- Total columns: 23
- Required columns validated: `sales`, `profit`

## 4. Monitoring Features
- Records application startup and dataset-loading events.
- Validates required columns and numeric values.
- Detects missing or invalid values in required fields.
- Assigns a unique ID to each monitoring request.
- Records request success and failure.
- Handles missing files, invalid CSV files, and unexpected exceptions.

## 5. Validation Results
The actual customer dataset loaded successfully and passed validation.

- Dataset validation: Successful
- Rows processed: 51,290
- Columns detected: 23
- Total sales recorded in the log: 12,642,905.00
- Total profit recorded in the log: 1,469,034.82
- Request status: Completed successfully

## 6. Issue Identified and Resolution
Initially, validation failed because the code expected `Sales` and `Profit`, while the dataset contains lowercase column names: `sales` and `profit`.

The validation code was updated to use the actual column names. The dataset then passed validation without modifying the original CSV.

## 7. Log File
Monitoring events are stored in `customer_monitoring.log` inside the `Day46` folder.

The log includes timestamps, validation results, request IDs, summary metrics, and error messages.

## 8. Conclusion
This exercise demonstrated how logging, validation, request tracking, and exception handling can improve the reliability and observability of a customer analytics application.

Future improvements could include automated alerts, dashboard health checks, and monitoring trends over time.