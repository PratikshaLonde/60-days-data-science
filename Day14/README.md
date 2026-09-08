# Day 14 — Adapting Models to Changing Constraints

## Objective

Understand how machine learning models adapt when an important feature becomes unavailable.

## What I Worked On

- Trained a baseline Linear Regression model
- Measured baseline performance
- Removed the important `sales` feature
- Retrained the model using the remaining features
- Compared performance before and after removing the feature
- Analyzed the impact on model performance
- Created a performance comparison visualization
- Wrote a Sprint 2 reflection

## Important Feature Removed

The `sales` feature was removed to simulate a real-world situation where an important input is no longer available.

## Performance After Removing Sales

- MAE: 0.3525
- R²: 0.3029

The model continued to make predictions using the remaining features, but its performance decreased after removing `sales`.

## Key Learning

Real-world machine learning systems often face changing requirements and missing features.

A model should be able to adapt when important inputs become unavailable.

The main lesson from Day 14 is:

**Machine learning models must be designed to handle changing real-world constraints.**

## Output Files

- `day14.ipynb` — Updated model notebook
- `performance_comparison.csv` — Before vs after performance
- `performance_before_after.png` — Performance visualization
- `README.md` — Sprint 2 documentation

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook