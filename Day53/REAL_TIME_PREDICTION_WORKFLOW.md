
# Real-Time Prediction Workflow

## Objective
To develop an interactive application that demonstrates how input data is processed by a trained regression model to generate immediate predictions.

## Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Workflow
1. Generate and prepare sample data.
2. Separate input features and target values.
3. Split the data into training and testing sets.
4. Train a Linear Regression model.
5. Collect input values through the Streamlit interface.
6. Generate predictions using the trained model.
7. Evaluate model performance using MAE, RMSE, and R².
8. Display results and visualizations.

## Application Modules
- Prediction
- Dataset Explorer
- Model Evaluation
- Workflow Overview

## Dataset
The application generates synthetic student-performance data for demonstration. It does not use real student records or a live external data source.

## Limitations
Predictions are illustrative and are not suitable for real student evaluation. The application demonstrates interactive inference but does not continuously receive live external data.

## Future Enhancements
- Integrate an appropriate real-world dataset.
- Add data validation and error handling.
- Connect a live data source where required.
- Add model comparison and monitoring.
- Deploy the application online.
