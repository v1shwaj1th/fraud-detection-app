from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("fraud_rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
selected_features = pickle.load(open("selected_features.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
input_options = pickle.load(open("input_options.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", options=input_options)

@app.route("/predict", methods=["POST"])
def predict():
    input_data = {}
    for feature in selected_features:
        input_data[feature] = request.form.get(feature)

    df_input = pd.DataFrame([input_data])

    # Encode categorical features
    for col in df_input.columns:
        if col in label_encoders:
            le = label_encoders[col]
            df_input[col] = le.transform(df_input[col])

    # Scale
    X_scaled = scaler.transform(df_input[selected_features])

    # Predict
    prediction = model.predict(X_scaled)[0]
    result = "Fraudulent Claim" if prediction == 1 else "Legitimate Claim"

    return render_template("result.html", result=result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
