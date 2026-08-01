# ❤️ Heart Disease Prediction using Machine Learning
## End-to-End Machine Learning Model Deployment using Flask and Render

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Render](https://img.shields.io/badge/Render-Deployed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Project Overview

Heart disease remains one of the leading causes of death worldwide. Early diagnosis can significantly improve treatment outcomes and reduce mortality. This project presents an **End-to-End Machine Learning application** that predicts the likelihood of heart disease based on various medical parameters.

The project demonstrates the complete machine learning lifecycle, beginning with data preprocessing and model training, followed by deployment of the trained model using **Flask** and **Render**. Users can enter patient health information through a web interface and instantly receive a prediction indicating whether heart disease is likely to be present.

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Build a Machine Learning model for heart disease prediction.
- Train and evaluate the model using real-world healthcare data.
- Save the trained model using Pickle.
- Develop a Flask web application for user interaction.
- Deploy the application online using Render.
- Demonstrate an end-to-end Machine Learning deployment workflow.

---

# 📊 Dataset

Dataset Used:

**Heart Disease Dataset**

Dataset Source:

https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

The dataset contains medical information collected from patients and is widely used for binary classification tasks.

---

# 📁 Dataset Features

| Feature | Description |
|----------|-------------|
| Age | Patient Age |
| Sex | Gender |
| ChestPainType | Chest Pain Category |
| RestingBP | Resting Blood Pressure |
| Cholesterol | Serum Cholesterol |
| FastingBS | Fasting Blood Sugar |
| RestingECG | Resting ECG Results |
| MaxHR | Maximum Heart Rate |
| ExerciseAngina | Exercise Induced Angina |
| Oldpeak | ST Depression |
| ST_Slope | ST Segment Slope |
| Target | Heart Disease (0 = No, 1 = Yes) |

---

# 🛠 Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-Learn
- Random Forest Classifier

## Web Framework

- Flask

## Data Processing

- Pandas
- NumPy

## Model Serialization

- Pickle

## Deployment

- GitHub
- Render

---

# 📚 Project Workflow

## Step 1 — Data Collection

The heart disease dataset is loaded using Pandas.

The dataset is inspected for:

- Missing values
- Data types
- Shape
- Summary statistics

---

## Step 2 — Data Preprocessing

The preprocessing pipeline includes:

- Feature Selection
- Target Selection
- Train-Test Split (80:20)
- Data Validation

---

## Step 3 — Model Training

A **Random Forest Classifier** is trained using the training dataset.

The model learns complex relationships between patient medical attributes and the presence of heart disease.

---

## Step 4 — Model Evaluation

The trained model is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## Step 5 — Model Serialization

The trained model is saved as

```
model.pkl
```

using Python Pickle.

---

## Step 6 — Flask Application

The Flask application

- Loads the trained model
- Accepts patient information
- Predicts heart disease
- Displays the result on a web page

---

## Step 7 — Deployment

The complete project is deployed on **Render**, making it publicly accessible through a web browser.

---

# 🧠 Machine Learning Model

This project uses

## Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Advantages

- High Accuracy
- Robust to Noise
- Handles Non-linear Data
- Resistant to Overfitting
- Fast Prediction

---

# 📈 Model Performance

> Replace the values below with your actual results after training the model.

| Evaluation Metric | Score |
|-------------------|------:|
| Accuracy | XX.XX% |
| Precision | XX.XX% |
| Recall | XX.XX% |
| F1-Score | XX.XX |

---

# 📊 Project Structure

```
Heart-Disease-Prediction-Deployment/

│
├── app.py
├── train_model.py
├── model.pkl
├── heart.csv
├── requirements.txt
├── README.md
├── render.yaml
├── Procfile
├── runtime.txt
│
├── templates/
│      └── index.html
│
├── static/
│      └── style.css
│
└── screenshots/
       ├── home_page.png
       └── prediction_page.png
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Heart-Disease-Prediction-Deployment.git
```

Move inside the project folder

```bash
cd Heart-Disease-Prediction-Deployment
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train_model.py
```

Run the Flask application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🌐 Render Deployment

The project can be deployed using Render.

Deployment Steps:

1. Push the project to GitHub.
2. Create a new Web Service on Render.
3. Connect your GitHub repository.
4. Set the Build Command:

```bash
pip install -r requirements.txt
```

5. Set the Start Command:

```bash
gunicorn app:app
```

6. Deploy.

After deployment, update the link below.

**Live Demo:**

```
https://your-render-url.onrender.com
```

---

# 📷 Screenshots

## Home Page

(Add Screenshot Here)

---

## Prediction Page

(Add Screenshot Here)

---

# 📌 Features

- End-to-End Machine Learning Project
- Flask Web Application
- Random Forest Prediction Model
- User-Friendly Interface
- Responsive Design
- Real-Time Prediction
- Deployment Ready
- GitHub Portfolio Project

---

# 🔮 Future Improvements

Possible improvements include:

- Hyperparameter tuning
- Feature engineering
- Cross-validation
- Model comparison (XGBoost, LightGBM)
- Probability-based prediction
- User authentication
- Database integration
- Docker containerization
- CI/CD pipeline
- Cloud deployment on AWS or Azure

---

# 💡 Conclusion

This project demonstrates the complete lifecycle of a Machine Learning application, from data preprocessing and model training to deployment as a web application. A Random Forest Classifier was trained to predict the likelihood of heart disease using patient medical information. The trained model was integrated into a Flask application, enabling users to enter patient details and receive real-time predictions through a user-friendly interface. Finally, the application was prepared for deployment on Render, making it accessible online. This project highlights practical skills in machine learning, web development, model serialization, and cloud deployment, providing a strong foundation for real-world AI and ML applications.

