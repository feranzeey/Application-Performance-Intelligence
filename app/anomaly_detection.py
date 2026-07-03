import pandas as pd
from sklearn.ensemble import IsolationForest

# Sample request counts
data = pd.DataFrame({
    "requests": [100, 110, 95, 105, 500]
})

# Train the model
model = IsolationForest(random_state=42)

# Predict anomalies
data["Prediction"] = model.fit_predict(data)

# Convert predictions to readable labels
data["Prediction"] = data["Prediction"].replace({
    1: "Normal",
    -1: "Anomaly"
})

print(data)