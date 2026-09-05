# Day 11 — Building Your First ML Pipeline

## Objective

Build a complete machine learning workflow from data preparation to generating predictions.

## What I Worked On

- Loaded the feature-engineered dataset
- Selected features and target
- Removed target leakage features
- Split the dataset into training and testing sets
- Trained a Linear Regression model
- Generated predictions
- Evaluated model performance using MAE and R² Score
- Saved prediction outputs

## Machine Learning Model

### Algorithm

Linear Regression

### Target

`profit`

The target is the scaled profit value from the feature-engineered dataset.

## Data Split

- Training data: 80%
- Testing data: 20%
- Random state: 42

## Model Evaluation

- Mean Absolute Error (MAE): **0.3428**
- R² Score: **0.3611**

The baseline model explains approximately **36.11% of the variation** in the target.

## Prediction Output

The predicted and actual values were saved in:

`prediction_outputs.csv`

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Key Learning

This exercise helped me understand the complete basic machine learning workflow:

**Prepare → Split → Train → Predict → Evaluate**

The first model does not need to be perfect. A baseline model provides a starting point for future improvements.

## Files

- `day11.ipynb` — Machine learning notebook
- `prediction_outputs.csv` — Actual and predicted values
- `README.md` — Project explanation