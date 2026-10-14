# Day50 — Model Optimization Report

## 1. Objective
Evaluate baseline model performance, optimize hyperparameters, compare algorithms, and examine generalization.

## 2. Dataset
- Records: 51,290
- Features: 49 after one-hot encoding
- Training records: 41,032
- Testing records: 10,258
- Target: Profit, Loss, and Break-even

## 3. Model Comparison

| Model | Accuracy | Macro F1-score |
|---|---:|---:|
| Baseline Decision Tree | 87.66% | 0.5924 |
| Optimized Decision Tree | 91.89% | 0.5989 |
| Random Forest | 63.38% | 0.5238 |

## 4. Optimization
GridSearchCV selected the following Decision Tree settings:

- Maximum depth: 5
- Minimum samples per leaf: 1
- Minimum samples to split: 2
- Class weight: None

The search optimized macro F1-score using three-fold cross-validation.

## 5. Generalization Analysis
- Training accuracy: 92.13%
- Testing accuracy: 91.89%
- Accuracy gap: 0.24 percentage points

The small accuracy gap suggests limited overfitting based on accuracy.

## 6. Key Findings
- The optimized Decision Tree achieved the highest accuracy and macro F1-score among the three tested models.
- Accuracy improved by 4.23 percentage points compared with the baseline Decision Tree.
- The macro F1-score improved only slightly, from 0.5924 to 0.5989.
- The optimized model did not identify any Break-even cases correctly.
- The tested Random Forest configuration performed worse than the Decision Tree models.

## 7. Limitations and Tradeoffs
The dataset has imbalanced target classes. High overall accuracy does not guarantee reliable performance for the minority Break-even class. Further class-specific evaluation and feature review are required before using the model for business decisions.

## 8. Conclusion
The optimized Decision Tree is the strongest model among the tested configurations, but its Break-even classification performance remains inadequate. Additional improvements should focus on minority-class detection and reliable evaluation rather than accuracy alone.
