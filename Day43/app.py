from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("customer_risk_model.pkl")

features = [
    "total_sales",
    "total_profit",
    "total_quantity",
    "number_of_orders",
    "average_discount",
    "average_shipping_days"
]

@app.route("/")
def home():
    return jsonify({
        "message": "Customer Risk Prediction API is running!"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    customer_data = pd.DataFrame([data])

    prediction = model.predict(
        customer_data[features]
    )[0]

    probability = model.predict_proba(
        customer_data[features]
    )[0][1]

    risk_level = "High Risk" if probability >= 0.60 else (
        "Medium Risk" if probability >= 0.30 else "Low Risk"
    )

    return jsonify({
        "churn_risk": int(prediction),
        "risk_probability": round(float(probability), 4),
        "risk_percentage": round(float(probability * 100), 2),
        "risk_level": risk_level
    })

if __name__ == "__main__":
    app.run(debug=True)