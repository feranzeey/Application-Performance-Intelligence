from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
traffic = np.array([100, 120, 140, 160, 180])

# Train the model
model = LinearRegression()
model.fit(hours, traffic)

# Predict traffic for hour 6
prediction = model.predict([[6]])

print(f"Predicted traffic for Hour 6: {prediction[0]:.0f} requests")