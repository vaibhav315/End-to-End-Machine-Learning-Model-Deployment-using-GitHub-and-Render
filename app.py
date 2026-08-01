# ============================================================
# Heart Disease Prediction Web Application
# AI-ML Final Project
# ============================================================

# -----------------------------
# Import Libraries
# -----------------------------

from flask import Flask, render_template, request
import pickle
import numpy as np

# -----------------------------
# Load Trained Model
# -----------------------------

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Initialize Flask App
# -----------------------------

app = Flask(__name__)

# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction Route
# -----------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Read values from HTML form
        age = float(request.form["age"])
        sex = float(request.form["sex"])
        cp = float(request.form["cp"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        fbs = float(request.form["fbs"])
        restecg = float(request.form["restecg"])
        thalach = float(request.form["thalach"])
        exang = float(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = float(request.form["slope"])
        ca = float(request.form["ca"])
        thal = float(request.form["thal"])

        # Arrange features in correct order
        features = np.array([[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]])

        # Predict
        prediction = model.predict(features)[0]

        # Output message
        if prediction == 1:
            result = "⚠️ Heart Disease Detected"
            color = "red"
        else:
            result = "✅ No Heart Disease Detected"
            color = "green"

        return render_template(
            "index.html",
            prediction_text=result,
            prediction_color=color
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction_text=f"Error: {e}",
            prediction_color="red"
        )


# -----------------------------
# Run Flask App
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)
