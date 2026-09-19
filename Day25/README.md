# Day 25 - Cross-Validation

## Building Reliable Models with Cross-Validation

### Objective
Evaluate machine learning models across multiple data splits to understand their performance and stability.

### Tasks Completed
- Applied 5-Fold Cross-Validation
- Evaluated Logistic Regression
- Evaluated Decision Tree
- Evaluated Random Forest
- Compared train-test accuracy with cross-validation accuracy
- Calculated mean CV accuracy
- Calculated CV standard deviation
- Analyzed model stability
- Created performance visualizations
- Saved the comparison report

### Models Evaluated
- Logistic Regression
- Decision Tree
- Random Forest

### Validation Method
5-Fold Cross-Validation was used with shuffling and a fixed random state for reproducible results.

### Files
- `day25.ipynb` - Cross-validation notebook
- `cross_validation_comparison.csv` - Model performance comparison
- `cross_validation_accuracy.png` - Mean CV accuracy visualization
- `model_stability.png` - Model stability visualization

### Key Learning
Cross-validation provides a more reliable estimate of model performance by evaluating a model across multiple train-test splits. Mean CV accuracy shows average performance, while standard deviation helps understand performance stability across folds.