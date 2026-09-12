# Day 18 - Fraud Detection Using Random Forest

## Objective
Build a Random Forest classifier to detect fraudulent transactions and compare it with a Decision Tree.

## Dataset
A small synthetic dataset was created for learning and demonstration.

## Features
- Transaction Amount
- Transaction Frequency
- Account Age Days
- International Transaction

## Target
- Fraud
  - 0 = Not Fraud
  - 1 = Fraud

## Models
- Decision Tree Classifier
- Random Forest Classifier

## Tasks Completed
- Created and explored fraud dataset
- Split data into training and testing sets
- Trained Random Forest
- Trained Decision Tree for comparison
- Generated predictions
- Evaluated model accuracy
- Created confusion matrices
- Generated classification reports
- Compared both models
- Analyzed Random Forest feature importance
- Checked training and testing performance
- Documented fraud detection challenges
- Saved prediction and comparison files

## Files
- `day18.ipynb`
- `model_comparison.csv`
- `fraud_predictions.csv`
- `random_forest_feature_importance.png`

## Key Learning
Random Forest combines multiple decision trees to make predictions and can provide more stable results than a single Decision Tree.

## Fraud Detection Challenges
Fraud detection involves challenges such as class imbalance, changing fraud patterns, costly missed fraud, and false positives.

## Note
This project uses a small synthetic dataset for learning and demonstration. It is not suitable for real-world fraud detection.