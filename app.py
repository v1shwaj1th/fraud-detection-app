from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import pandas as pd

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session storage

# Load ML components
model = pickle.load(open("fraud_rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
selected_features = pickle.load(open("selected_features.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
input_options = pickle.load(open("input_options.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        input_data = {feature: request.form.get(feature) for feature in selected_features}
        df_input = pd.DataFrame([input_data])

        for col in df_input.columns:
            if col in label_encoders:
                le = label_encoders[col]
                df_input[col] = le.transform(df_input[col])

        X_scaled = scaler.transform(df_input[selected_features])
        prediction = model.predict(X_scaled)[0]
        result = "Fraudulent Claim" if prediction == 1 else "Legitimate Claim"

        # Store result in session and redirect
        session["result"] = result
        return redirect(url_for("result_page"))

    return render_template("predict.html", options=input_options, result=None)

@app.route("/result")
def result_page():
    result = session.get("result", None)
    if result is None:
        return redirect(url_for("predict"))
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
