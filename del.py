import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Example Data
crop_yield_data = {
    'Crop': ['Wheat', 'Rice', 'Corn', 'Soybean'],
    'Predicted Yield': [3.0, 4.2, 3.5, 2.8],
    'Actual Yield': [2.9, 4.1, 3.4, 2.7]
}

soil_health_data = {
    'Region': ['North', 'South', 'East', 'West'],
    'Nitrogen': [60, 55, 70, 65],
    'Phosphorus': [40, 45, 35, 50],
    'Potassium': [80, 85, 75, 90]
}

weather_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [5, 7, 10, 15, 20, 25, 30, 28, 24, 18, 12, 7],
    'Precipitation': [50, 45, 60, 55, 70, 75, 80, 65, 60, 55, 50, 45]
}

market_price_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Wheat': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Rice': [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410]
}

pest_disease_data = {
    'Disease': ['Blight', 'Mildew', 'Rust', 'Wilt'],
    'Occurrences': [40, 30, 20, 10]
}

# Convert to DataFrame
df_crop_yield = pd.DataFrame(crop_yield_data)
df_soil_health = pd.DataFrame(soil_health_data)
df_weather = pd.DataFrame(weather_data)
df_market_price = pd.DataFrame(market_price_data)
df_pest_disease = pd.DataFrame(pest_disease_data)

# Plot Crop Yield Predictions
plt.figure(figsize=(10, 6))
sns.barplot(x='Crop', y='value', hue='variable', data=pd.melt(df_crop_yield, ['Crop']))
plt.title('Predicted vs. Actual Crop Yield')
plt.ylabel('Yield (tons per hectare)')
plt.show()

# Plot Soil Health Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df_soil_health.set_index('Region'), annot=True, cmap='YlGnBu')
plt.title('Soil Health Nutrient Levels')
plt.ylabel('Region')
plt.xlabel('Nutrient Levels (mg/kg)')
plt.show()

# Plot Weather Trends
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)', color='tab:blue')
ax1.plot(df_weather['Month'], df_weather['Temperature'], color='tab:blue', label='Temperature')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax2 = ax1.twinx()
ax2.set_ylabel('Precipitation (mm)', color='tab:green')
ax2.plot(df_weather['Month'], df_weather['Precipitation'], color='tab:green', label='Precipitation')
ax2.tick_params(axis='y', labelcolor='tab:green')
fig.tight_layout()
plt.title('Monthly Weather Trends')
plt.show()

# Plot Market Prices
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='value', hue='variable', data=pd.melt(df_market_price, ['Month']))
plt.title('Historical and Forecasted Crop Prices')
plt.ylabel('Price (USD per ton)')
plt.show()

# Plot Pest and Disease Occurrences
plt.figure(figsize=(10, 6))
plt.pie(df_pest_disease['Occurrences'], labels=df_pest_disease['Disease'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribution of Crop Diseases')
plt.axis('equal')
plt.show()
