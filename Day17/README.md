# Day 17 - Loan Approval Prediction Using Decision Tree

## Objective
Build a Decision Tree classification model to predict whether a loan will be approved.

## Dataset
A small synthetic demonstration dataset was created for this challenge.

## Features
- Income
- Credit Score
- Loan Amount
- Employment Years

## Target
- Loan Approved
  - 0 = Not Approved
  - 1 = Approved

## Model
Decision Tree Classifier

The model uses `max_depth=3` to control tree complexity and reduce overfitting.

## Tasks Completed
- Created and explored the loan dataset
- Separated features and target
- Split data into training and testing sets
- Trained a Decision Tree classifier
- Evaluated model predictions
- Created a confusion matrix
- Visualized the Decision Tree
- Analyzed feature importance
- Checked training and testing accuracy
- Extracted decision rules
- Saved prediction results

## Files
- `day17.ipynb` - Main notebook
- `decision_tree.png` - Decision Tree visualization
- `feature_importance.png` - Feature importance graph
- `loan_predictions.csv` - Prediction results

## Key Learning
Decision Trees make predictions by applying a sequence of feature-based rules. Feature importance helps identify which variables contribute most to the model's decisions.

## Overfitting
Decision Trees can overfit when they become too complex. Limiting the tree depth is one way to control model complexity.

## Real-World Impact
Decision-based models can support automated loan screening and risk assessment in financial applications.

## Note
This project uses a small synthetic dataset for learning and demonstration. It is not intended for real-world lending decisions.