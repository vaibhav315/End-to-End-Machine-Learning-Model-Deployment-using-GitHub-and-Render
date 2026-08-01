# ============================================================
# Heart Disease Prediction Model Training
# AI-ML Final Project
# ============================================================

# -----------------------------
# Import Libraries
# -----------------------------

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# -----------------------------
# Load Dataset
# -----------------------------

print("="*60)
print("Loading Dataset...")
print("="*60)

df = pd.read_csv("heart.csv")

print("\nFirst Five Records\n")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# Feature Selection
# -----------------------------

X = df.drop("target", axis=1)
y = df["target"]

print("\nInput Features")
print(X.columns)

print("\nTarget Variable")
print("target")

# -----------------------------
# Train-Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples :", X_test.shape[0])

# -----------------------------
# Model Development
# -----------------------------

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Completed!")

# -----------------------------
# Prediction
# -----------------------------

y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score")
print(f"{accuracy:.4f}")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully as model.pkl")

# -----------------------------
# Feature Order
# -----------------------------

print("\nFeature Order (Use this order in app.py):")

for feature in X.columns:
    print(feature)

print("\nProject Ready for Deployment!")
