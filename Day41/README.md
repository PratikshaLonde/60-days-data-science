readme = """# Day 41/60 — Predicting High-Risk Customers Before They Churn

## Objective

Build a predictive customer risk system that identifies customers who may be at high risk of churn and recommends suitable retention strategies.

## What I Worked On

- Customer behavior analysis
- Churn-risk signal creation
- Predictive classification
- Random Forest model
- Churn probability prediction
- Customer risk ranking
- High-risk customer identification
- Risk visualization
- Feature importance analysis
- Retention strategy recommendations

## Risk Levels

- Low Risk: 0–30%
- Medium Risk: 30–60%
- High Risk: 60–100%

## Model

Random Forest Classifier was used to predict customer churn risk based on historical customer behavior.

## Output Files

- day41.ipynb
- customer_risk_ranking.csv
- risk_feature_importance.csv
- business_recommendation_report.md
- README.md

## Business Value

The system helps businesses identify customers who may require attention and prioritize retention activities based on predicted risk.

## Limitations

The churn labels are created using historical purchase behavior and the model should be treated as a risk indicator rather than a guaranteed churn prediction.

## Tools Used

Python, Pandas, NumPy, Matplotlib, Scikit-learn
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print("README created successfully!")