import pandas as pd
import joblib
import numpy as np
import os
import warnings

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# ----------------------------
# Suppress warnings
# ----------------------------
warnings.filterwarnings("ignore")

# ----------------------------
# Load dataset
# ----------------------------
df = pd.read_csv("Housing.csv")
df = df.dropna()

# ----------------------------
# One-Hot Encoding
# ----------------------------
df = pd.get_dummies(df, columns=[
    'mainroad', 'guestroom', 'basement',
    'hotwaterheating', 'airconditioning',
    'prefarea', 'furnishingstatus'
], drop_first=True)

# ----------------------------
# Features & Target
# ----------------------------
X = df.drop("price", axis=1)
y = df["price"]

# ----------------------------
# Train-Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# Train Model
# ----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ----------------------------
# Predictions
# ----------------------------
y_pred = model.predict(X_test)

# ----------------------------
# Evaluation Metrics
# ----------------------------
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

# Safe MAPE calculation (avoid division by zero)
epsilon = 1e-10
mape = np.mean(np.abs((y_test - y_pred) / (y_test + epsilon))) * 100

# Accuracy-like metric
accuracy = 100 - mape

# ----------------------------
# Print Results
# ----------------------------
print("\n📊 Model Performance:")
print(f"R² Score        : {r2:.4f}")
print(f"RMSE            : {rmse:.2f}")
print(f"MAE             : {mae:.2f}")
print(f"MAPE            : {mape:.2f}%")
print(f"Accuracy (~%)   : {accuracy:.2f}%")

# ----------------------------
# Save Model
# ----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(
    {
        "model": model,
        "features": X.columns.tolist()
    },
    "models/house_price_model.joblib"
)

print("\n✅ Model saved at: models/house_price_model.joblib")
