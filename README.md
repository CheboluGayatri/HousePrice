# 🏡 House Price Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)

A Machine Learning web application that predicts residential house prices using property characteristics such as area, number of bedrooms, bathrooms, parking availability, furnishing status, and additional amenities.

The project demonstrates an end-to-end Machine Learning workflow, including data preprocessing, feature engineering, model training, evaluation, model persistence, and deployment as an interactive web application using Streamlit.

---

# 🌐 Live Demo

**Application:**  
https://houseprice-kcvnxs5sxgawny4wzehj52.streamlit.app/

---

# 📖 Project Overview

The House Price Prediction application uses a **Linear Regression** model trained on housing data to estimate property prices based on user-provided inputs.

The application provides an intuitive web interface where users can enter property details and receive an estimated house price instantly.

This project demonstrates practical implementation of:

- Data preprocessing
- Feature engineering
- Machine Learning model training
- Regression analysis
- Model evaluation
- Model deployment
- Interactive web application development

---

# ✨ Key Features

- Real-time house price prediction
- Interactive Streamlit interface
- Responsive and user-friendly design
- Data preprocessing and feature engineering
- One-Hot Encoding for categorical variables
- Automatic feature alignment with the trained model
- Model serialization using Joblib
- Robust error handling
- Fast prediction using a pre-trained model
- Cloud deployment with Streamlit Community Cloud

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Programming Language** | Python 3 |
| **Machine Learning** | Scikit-learn, Linear Regression |
| **Data Processing** | Pandas, NumPy |
| **Data Preprocessing** | Data Cleaning, Missing Value Handling, One-Hot Encoding, Feature Engineering |
| **Model Training** | Train-Test Split, Linear Regression |
| **Model Evaluation** | R² Score, RMSE, MAE, MAPE |
| **Model Persistence** | Joblib |
| **Web Framework** | Streamlit |
| **Frontend/UI** | Streamlit Components, HTML, CSS |
| **Development Environment** | Visual Studio Code |
| **Version Control** | Git, GitHub |
| **Deployment Platform** | Streamlit Community Cloud |
| **Package Manager** | pip |
| **Dataset Format** | CSV |
| **Saved Model Format** | Joblib (.joblib) |

---

# 🔄 Machine Learning Workflow

```text
Housing Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
One-Hot Encoding
        │
        ▼
Train-Test Split
        │
        ▼
Linear Regression Model
        │
        ▼
Model Evaluation
        │
        ▼
Save Trained Model
        │
        ▼
Streamlit Web Application
        │
        ▼
Real-Time House Price Prediction
```

---

# 📂 Project Structure

```text
House-Price-Prediction/
│
├── models/
│   └── house_price_model.joblib
│
├── app.py
├── train_model.py
├── Housing.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📥 Input Features

The prediction model uses the following property attributes:

| Feature | Description |
|---------|-------------|
| Area | Total house area (sq.ft.) |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Stories | Number of floors |
| Parking | Available parking spaces |
| Main Road | Road accessibility |
| Guest Room | Guest room availability |
| Basement | Basement availability |
| Hot Water Heating | Heating facility |
| Air Conditioning | Air conditioning availability |
| Preferred Area | Preferred residential area |
| Furnishing Status | Furnished, Semi-Furnished, Unfurnished |

---

# 📈 Model Evaluation

The trained model is evaluated using standard regression metrics:

- **R² Score**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**
- **Mean Absolute Percentage Error (MAPE)**
- **Approximate Prediction Accuracy**

These metrics help assess prediction accuracy and overall model performance.

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

## Navigate to the Project

```bash
cd House-Price-Prediction
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 📦 Required Packages

```text
pandas>=1.3
numpy>=1.21
scikit-learn>=1.0
joblib>=1.1
streamlit>=1.25
```

---

# ☁️ Deployment

**Platform:** Streamlit Community Cloud

### Deployment Process

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select `app.py` as the application entry point.
5. Install dependencies from `requirements.txt`.
6. Deploy the application.

**Live Application**

https://houseprice-kcvnxs5sxgawny4wzehj52.streamlit.app/

---

# 🎯 Future Enhancements

- Random Forest Regression
- XGBoost Regression
- Hyperparameter Tuning
- Interactive Data Visualizations
- Feature Importance Analysis
- Model Comparison Dashboard
- Location-Based House Price Prediction
- REST API Integration
- Docker Support
- CI/CD Pipeline
- Cloud Database Integration

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Submit a Pull Request.

---

# 👩‍💻 Author

**Gayatri**

- **Portfolio:** https://your-portfolio.com
- **GitHub:** https://github.com/your-username
- **LinkedIn:** https://linkedin.com/in/your-profile

---
If you found this project useful, consider giving it a **Star** on GitHub.
