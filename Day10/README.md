# Day 10 — Transforming Raw Data into Better Signals

## Objective

Transform raw data into machine-learning-ready features using feature engineering techniques.

## What I Worked On

- Identified numerical and categorical features
- Created derived features
- Applied One-Hot Encoding to categorical features
- Scaled numerical features using StandardScaler
- Handled infinity values
- Compared the dataset before and after feature engineering
- Created a final machine-learning-ready dataset

## Derived Features

Two new features were created:

1. `sales_per_shipping_day`
2. `profit_per_sales`

## Feature Encoding

Categorical features such as:

- Category
- Segment
- Region

were converted into numerical features using One-Hot Encoding.

## Feature Scaling

Numerical features were standardized using `StandardScaler`.

## Model Readiness

### Before Feature Engineering

- Rows: 51,290
- Columns: 25
- Categorical columns: 15
- Numerical columns: 10

### After Feature Engineering

- Rows: 51,289
- Columns: 29
- All features numeric: Yes
- Missing values: 0

One invalid row containing an infinity value was removed during preprocessing.

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Key Learning

Feature engineering helps transform raw data into meaningful numerical signals that can be used more effectively by machine learning models.

The main lesson from Day 10 is:

**Better features can lead to better machine learning inputs.**