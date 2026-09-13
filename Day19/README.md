# Day 19 - Boosting Model Performance with XGBoost

## Objective
Build an XGBoost boosting model and compare its performance with Random Forest.

## Dataset
A small synthetic fraud detection dataset was created for learning and demonstration.

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
- Random Forest Classifier
- XGBoost Classifier

## Tasks Completed
- Installed and configured XGBoost
- Created the fraud detection dataset
- Trained Random Forest
- Trained XGBoost
- Compared model performance
- Analyzed XGBoost feature importance
- Checked training and testing accuracy
- Documented boosting advantages and trade-offs
- Saved prediction results

## Model Comparison

On this small demonstration dataset:
- Random Forest Accuracy: 1.000
- XGBoost Accuracy: 0.667

These results should not be treated as reliable real-world performance because the dataset contains only a small number of synthetic records.

## Key Learning
Boosting builds models step-by-step to improve predictions. XGBoost is powerful for structured data but may require more tuning and can overfit when model complexity is too high.

## Fraud Detection Challenges
- Class imbalance
- False positives
- Missed fraudulent transactions
- Changing fraud patterns
- Need for large, high-quality real-world data

## Files
- `day19.ipynb`
- `model_comparison.csv`
- `xgboost_feature_importance.png`
- `fraud_predictions.csv`

## Note
This project uses a small synthetic dataset created only for learning and demonstration. It is not suitable for real-world fraud detection.