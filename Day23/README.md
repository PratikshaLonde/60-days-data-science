# Day 23 - Feature Selection

## Finding the Most Important Signals in Data

### Objective
Identify important features that contribute to prediction quality and remove lower-impact features to reduce model complexity.

### Tasks Completed
- Analyzed correlations between numerical features
- Created a correlation heatmap
- Trained a baseline Logistic Regression model
- Calculated feature importance using model coefficients
- Selected important features based on their importance
- Trained a model using selected features
- Compared accuracy before and after feature selection
- Saved feature importance and comparison results
- Created feature importance and performance visualizations

### Features Analyzed
- Sales
- Quantity
- Discount
- Shipping Cost
- Shipping Days

### Model
Logistic Regression was used as the baseline classification model.

### Files
- `day23.ipynb` - Feature selection notebook
- `feature_importance.csv` - Feature importance results
- `feature_selection_comparison.csv` - Performance comparison
- `feature_importance.png` - Feature importance visualization
- `feature_selection_comparison.png` - Accuracy comparison graph

### Key Learning
Feature selection helps machine learning models focus on useful signals while reducing unnecessary features and model complexity.