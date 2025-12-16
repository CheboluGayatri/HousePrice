# House Price Prediction using Machine Learning
#  Project Overview

This project predicts house prices based on various property features using a Machine Learning model. It uses Linear Regression for price prediction and a Streamlit web application to provide an interactive user interface where users can input house details and get an estimated price instantly.

The project demonstrates the complete ML workflow, from data preprocessing and model training to deployment as a user facing application.

# 🎯 Problem Statement

House prices depend on multiple factors such as area, number of bedrooms, location preferences, and amenities. Manually estimating prices can be inconsistent and time consuming. This project aims to build a data driven solution that predicts house prices accurately based on historical data.

# 🧠 Machine Learning Approach

Model Used: Linear Regression

Reason: Simple, interpretable, and effective as a baseline model for regression problems

Task Type: Supervised Regression

# 📂 Dataset Information

Dataset Name: Housing.csv

Target Variable: price

Features Include:

Area (sq ft)

Bedrooms

Bathrooms

Stories

Parking

Main road access

Guest room

Basement

Hot water heating

Air conditioning

Preferred area

Furnishing status

Data Preprocessing

Removed missing values

Converted categorical variables using One Hot Encoding

Ensured feature consistency between training and prediction

# ⚙️ Project Structure

├── Housing.csv
├── train.py # Model training and evaluation
├── app.py # Streamlit web application
├── models/
│ └── house_price_model.joblib
├── requirements.txt
└── README.md

# 🚀 Model Training

The model is trained using an 80 20 train test split.

# Evaluation Metrics

R² Score to measure goodness of fit

RMSE to measure prediction error in actual price units

After training, the model and feature names are saved using joblib for reuse in the Streamlit app.

# 🖥️ Web Application (Streamlit)

The Streamlit app allows users to:

Enter house details using a clean sidebar UI

Predict house price with a single click

View results instantly

# Features

Interactive UI

Error handling for missing or mismatched features

Custom styling for better user experience

# 🛠️ Installation and Setup
1️⃣ Clone the Repository

2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train the Model 
python train.py
4️⃣ Run the Streamlit App
streamlit run app.py --server.port 8501
Sample Output

Estimated House Price displayed in Indian Rupees

Based on user selected features

# 🔐 Error Handling

Checks if model file exists

Prevents prediction if feature mismatch occurs

Displays user friendly error messages

# 🔮 Future Improvements

Try advanced models like Random Forest or XGBoost

Perform feature scaling and outlier handling

Add location based features

Deploy using Streamlit Cloud or Docker

Convert into REST API using FastAPI

# 📚 Skills Demonstrated

Data preprocessing and feature engineering

Supervised machine learning

Model evaluation and persistence

Streamlit based deployment

End to end ML project implementation
# 🌐 Live Demo
The application is deployed using Streamlit Cloud and is accessible at:
https://houseprice-kcvnxs5sxgawny4wzehj52.streamlit.app/
ny updates pushed to the main branch are automatically reflected in the live app.
