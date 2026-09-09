# Day 15 — Predicting Customer Churn with Logistic Regression

## Objective

Build a classification model to predict whether a customer is likely to churn using Logistic Regression.

## Dataset

The project uses the Telco Customer Churn dataset.

The target variable is:

- `Churn`
  - `No` = 0
  - `Yes` = 1

## What I Worked On

- Loaded the customer churn dataset
- Explored the dataset columns
- Checked for missing values
- Identified features and target
- Converted the target into numerical values
- Applied one-hot encoding to categorical features
- Split the data into training and testing sets
- Trained a Logistic Regression classifier
- Generated predictions on unseen data
- Evaluated model accuracy
- Created a confusion matrix
- Analyzed false positives and false negatives
- Saved prediction results

## Model Used

### Logistic Regression

Logistic Regression was used as the classification algorithm to predict whether a customer would churn.

## Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Business Implications

### False Positives

A false positive occurs when the model predicts that a customer will churn, but the customer actually stays.

This may cause the company to spend retention resources unnecessarily.

### False Negatives

A false negative occurs when the model predicts that a customer will stay, but the customer actually churns.

This can be more costly because the company may miss an opportunity to retain a customer and potentially lose revenue.

## Key Learning

Customer churn prediction is not only about model accuracy.

Different prediction errors can have different business costs. For churn prediction, improving recall for the churn class can help identify more customers who are at risk of leaving.

## Output Files

- `day15.ipynb` — Classification notebook
- `prediction_results.csv` — Model predictions
- `confusion_matrix.png` — Confusion matrix visualization
- `README.md` — Project documentation

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Key Takeaway

**Machine Learning can help businesses identify customers at risk of leaving and take action before they churn.**