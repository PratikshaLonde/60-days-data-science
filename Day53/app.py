
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.set_page_config(
    page_title="Real-Time Prediction Workflow",
    page_icon="📊",
    layout="wide"
)

@st.cache_resource
def train_model():
    rng = np.random.default_rng(42)

    data = pd.DataFrame({
        "Hours_Studied": rng.uniform(1, 10, 200),
        "Attendance": rng.uniform(50, 100, 200),
        "Previous_Score": rng.uniform(30, 95, 200)
    })

    data["Final_Score"] = (
        3.5 * data["Hours_Studied"]
        + 0.25 * data["Attendance"]
        + 0.45 * data["Previous_Score"]
        + rng.normal(0, 4, 200)
    ).clip(0, 100)

    features = ["Hours_Studied", "Attendance", "Previous_Score"]
    X = data[features]
    y = data["Final_Score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    metrics = {
        "mae": mean_absolute_error(y_test, predictions),
        "rmse": np.sqrt(mean_squared_error(y_test, predictions)),
        "r2": r2_score(y_test, predictions)
    }

    return model, data, X_test, y_test, predictions, metrics


model, data, X_test, y_test, test_predictions, metrics = train_model()

st.title("📊 Real-Time Prediction Workflow")
st.caption("An interactive demonstration of data collection, model training, prediction, and evaluation.")

st.info(
    "This educational application uses synthetic student-performance data. "
    "Its predictions are illustrative and should not be used to evaluate real students."
)

st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Choose a section",
    ["Prediction", "Dataset Explorer", "Model Evaluation", "Workflow"]
)

if page == "Prediction":
    st.header("Make a Prediction")
    st.write("Adjust the input features and generate a prediction instantly.")

    col1, col2, col3 = st.columns(3)

    with col1:
        hours = st.number_input(
            "Hours Studied",
            min_value=0.0,
            max_value=24.0,
            value=5.0,
            step=0.5
        )

    with col2:
        attendance = st.number_input(
            "Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=1.0
        )

    with col3:
        previous_score = st.number_input(
            "Previous Score",
            min_value=0.0,
            max_value=100.0,
            value=70.0,
            step=1.0
        )

    if st.button("Generate Prediction", type="primary"):
        input_data = pd.DataFrame({
            "Hours_Studied": [hours],
            "Attendance": [attendance],
            "Previous_Score": [previous_score]
        })

        prediction = float(model.predict(input_data)[0])
        prediction = float(np.clip(prediction, 0, 100))

        st.subheader("Prediction Result")
        st.metric("Illustrative Predicted Score", f"{prediction:.2f} / 100")

        if prediction >= 75:
            st.success("The model's estimated score is in the higher range.")
        elif prediction >= 50:
            st.info("The model's estimated score is in the middle range.")
        else:
            st.warning("The model's estimated score is in the lower range.")

        st.write("Input values")
        st.dataframe(input_data, use_container_width=True)

        st.caption(
            "This result comes from a model trained on generated data. "
            "It is not a reliable prediction of an actual student's performance."
        )

elif page == "Dataset Explorer":
    st.header("Dataset Explorer")
    st.write("Explore the synthetic dataset used to demonstrate model training.")

    st.dataframe(data.head(20), use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(data))
    col2.metric("Total Features", 3)
    col3.metric("Target Variable", "Final Score")

    st.subheader("Summary Statistics")
    st.dataframe(data.describe(), use_container_width=True)

    st.subheader("Feature Relationships")
    st.bar_chart(data[["Hours_Studied", "Attendance", "Previous_Score", "Final_Score"]].corr()["Final_Score"].drop("Final_Score"))

elif page == "Model Evaluation":
    st.header("Model Evaluation")

    col1, col2, col3 = st.columns(3)
    col1.metric("Mean Absolute Error", f"{metrics['mae']:.2f}")
    col2.metric("Root Mean Squared Error", f"{metrics['rmse']:.2f}")
    col3.metric("R² Score", f"{metrics['r2']:.3f}")

    results = pd.DataFrame({
        "Actual Score": y_test.reset_index(drop=True),
        "Predicted Score": test_predictions
    })

    st.subheader("Actual vs Predicted")
    st.dataframe(results.head(20), use_container_width=True)

    fig, ax = plt.subplots()
    ax.scatter(results["Actual Score"], results["Predicted Score"])
    ax.set_xlabel("Actual Score")
    ax.set_ylabel("Predicted Score")
    ax.set_title("Actual vs Predicted Scores")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)

    st.caption("Evaluation results are based on the synthetic test dataset.")

elif page == "Workflow":
    st.header("Prediction Workflow")

    steps = [
        ("1. Data Collection", "Generate example feature and target data."),
        ("2. Data Preparation", "Separate the input features from the target."),
        ("3. Train-Test Split", "Reserve test data for model evaluation."),
        ("4. Model Training", "Fit a linear regression model on training data."),
        ("5. Input Collection", "Collect new feature values from the interface."),
        ("6. Prediction", "Use the trained model to calculate an estimated score."),
        ("7. Evaluation", "Measure error and R² on held-out test data."),
        ("8. Visualization", "Display predictions, metrics, and charts.")
    ]

    for title, description in steps:
        st.markdown(f"**{title}**")
        st.write(description)
        st.divider()

    st.subheader("Model Information")
    st.write("Algorithm: Linear Regression")
    st.write("Training data: Generated synthetic data")
    st.write("Prediction target: Illustrative final score")
    st.write("Input features: Study hours, attendance, previous score")

st.sidebar.divider()
st.sidebar.caption("Day53 | 60 Days Coding Challenge")
