# Day 12 — Teaching Machines to Predict Numbers

## Objective

Build a Linear Regression model to predict continuous numerical values and understand the relationship between input and output variables.

## What I Worked On

- Loaded the cleaned dataset
- Selected Sales as the input feature
- Selected Profit as the target
- Split the data into training and testing sets
- Trained a Linear Regression model
- Generated predictions
- Visualized the regression line
- Visualized prediction errors
- Interpreted model coefficients
- Evaluated prediction accuracy

## Model

### Algorithm

Linear Regression

### Input

`sales`

### Target

`profit`

## Model Evaluation

- Mean Absolute Error (MAE): **55.2924**
- R² Score: **0.3213**

The model explains approximately **32.13% of the variation in profit**.

## Visualizations

### Sales vs Profit

`sales_profit_regression.png`

This visualization shows the actual profit values and the regression line learned by the model.

### Prediction Errors

`prediction_errors.png`

This visualization shows the difference between predicted and actual profit values.

## Prediction Output

The actual and predicted profit values were saved in:

`prediction_results.csv`

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Key Learning

Linear Regression helps understand the relationship between an input variable and a continuous numerical target.

The main workflow was:

**Input → Train → Predict → Visualize → Evaluate**

## Conclusion

This exercise helped me understand how machines can learn numerical relationships from data and use those relationships to make predictions.