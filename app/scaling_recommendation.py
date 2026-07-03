from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
traffic = np.array([100, 120, 140, 160, 180])

# Train the model
model = LinearRegression()
model.fit(hours, traffic)

# Predict traffic for Hour 6
predicted = model.predict([[6]])[0]

print(f"Predicted traffic: {predicted:.0f} requests")

# Scaling recommendation
if predicted > 180:
    print("Recommendation: Scale up application by 2 instances")
else:



    
    print("Recommendation: Current capacity is sufficient")