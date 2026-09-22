# Day 28 - Building Your Most Optimized ML System Yet

## Sprint Review & Optimization

### Objective

Combine preprocessing, validation, and hyperparameter tuning techniques into a reproducible Machine Learning pipeline and compare its performance with the original pipeline.

## Real-World Problem

The goal is to predict whether a sales order will generate positive profit.

The model uses sales-related features to classify orders as:

- `1` - Positive profit
- `0` - Zero or negative profit

## Features Used

The following features were used:

- Sales
- Quantity
- Discount
- Shipping Cost
- Shipping Days

## ML Pipeline

The final pipeline combines:

1. StandardScaler
2. Random Forest Classifier
3. Cross-Validation
4. Hyperparameter Tuning

### Workflow

```text
Sales Dataset
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
StandardScaler
     ↓
Random Forest
     ↓
5-Fold Cross-Validation
     ↓
GridSearchCV
     ↓
Optimized Pipeline
     ↓
Test Performance