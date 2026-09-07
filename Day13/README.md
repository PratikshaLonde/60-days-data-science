# Day 13 — Preventing Models from Memorizing Data

## Objective

Understand overfitting and regularization by comparing Linear Regression, Ridge Regression, and Lasso Regression models.

## What I Worked On

* Trained a baseline Linear Regression model
* Trained Ridge Regression
* Trained Lasso Regression
* Generated training and testing predictions
* Compared Train vs Test MAE
* Compared Train vs Test R²
* Analyzed the R² gap to identify possible overfitting
* Visualized model performance
* Saved the model comparison results

## Models Used

### Linear Regression

Used as the baseline model for comparison.

### Ridge Regression

Ridge Regression uses L2 regularization to reduce model complexity and help prevent overfitting.

### Lasso Regression

Lasso Regression uses L1 regularization and can reduce the impact of less important features.

## Model Evaluation

The models were evaluated using:

* Mean Absolute Error (MAE)
* R² Score

Training and testing performance were compared to understand how well each model generalizes to unseen data.

## Overfitting Analysis

A large difference between Train R² and Test R² can indicate overfitting.

Regularization techniques such as Ridge and Lasso can help control model complexity and improve generalization.

## Output Files

* `day13.ipynb` — Model comparison notebook
* `model_comparison.csv` — Performance comparison
* `model_performance_comparison.png` — Train vs Test R² visualization
* `README.md` — Project documentation

## Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook

## Key Learning

The main lesson from Day 13 is:

**A model should not simply memorize training data. It should learn patterns that generalize to unseen data.**

Regularization provides an important way to control model complexity and reduce overfitting.
