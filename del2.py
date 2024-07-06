import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Example dataset
data = {
    'Nitrogen': [60, 55, 70, 65, 80, 75, 85],
    'Phosphorus': [40, 45, 35, 50, 60, 55, 65],
    'Potassium': [80, 85, 75, 90, 100, 95, 105],
    'Temperature': [15, 20, 18, 22, 30, 28, 25],
    'Precipitation': [55, 70, 60, 75, 80, 65, 85],
    'Yield': [2.9, 3.4, 3.0, 3.5, 4.2, 3.8, 4.0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Precipitation']]
y = df['Yield']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Example prediction
new_data = np.array([[70, 50, 85, 25, 65]])  # Example new input
predicted_yield = model.predict(new_data)
print(f"Predicted Crop Yield: {predicted_yield[0]} tons per hectare")
