# Day 21 - Choosing the Best Model Like a Real Data Scientist

## Objective
Compare classification models and select the best model for a real-world business problem.

## Models Compared
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## Model Selection
The final model was selected based mainly on F1 Score because it balances Precision and Recall.

## Business Considerations
Model selection should not depend only on accuracy. A real data scientist should also consider:

- Interpretability
- Reliability
- Scalability
- False positives
- False negatives
- Business impact

For fraud detection, missing fraudulent transactions can be costly. Therefore, Recall and F1 Score are important metrics.

## Week 3 Reflection
During Week 3, I learned how to build, evaluate and compare classification models. I learned that different models have different strengths and weaknesses. I also learned that choosing a model requires considering both technical performance and business requirements.

## Files
- `day21.ipynb`
- `final_model_comparison.csv`
- `model_f1_comparison.png`

## Note
The fraud dataset used in this project is a small synthetic dataset created for learning and demonstration.