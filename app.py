import streamlit as st
import joblib
import numpy as np

# Load the saved model 
model = joblib.load('model.joblib')

# Define the user inputs
st.title("House Price Prediction in California")

st.write("Please enter the details to get the predicted house value")

# Latitude and Longitude input
st.write("Please enter the latitude and the longitude of your preferred house.")
latitude = st.slider("Latitude", 32.5, 42.0, step=0.1, help="Select the latitude of the area where you want to buy the house.")
longitude = st.slider("Longitude", -124.5, -114.0, step=0.1, help="Select the longitude of the area where you want to buy the house.")

# Other features
st.write("Please provide additional information about the area and the house.")
housing_median_age = st.number_input("Housing Median Age", min_value=1, max_value=100, value=25, help="Enter the median age of the houses in the area.")
total_rooms = st.number_input("Total Rooms in the Houses of that Area", min_value=1, max_value=10000, value=1000, help="Enter the total number of rooms in the houses in the area.")
total_bedrooms = st.number_input("Total Bedrooms in the Houses of your Preferred Area", min_value=1, max_value=5000, value=200, help="Enter the total number of bedrooms in the houses in the area.")
population = st.number_input("Estimated Population of the Area you want to buy your house in", min_value=1, max_value=50000, value=1000, help="Enter the estimated population of the area.")
households = st.number_input("Households", min_value=1, max_value=5000, value=300, help="Enter the number of households in the area.")
median_income = st.number_input("Median Income of the People living in that Area", min_value=0.0, max_value=20.0, value=5.0, help="Enter the median income of the residents in the area.")

# Ocean proximity with a select box for multi-categorical data
st.write("Please select the proximity of the house to the ocean.")
ocean_proximity = st.selectbox("Ocean Proximity", ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], help="Select the ocean proximity category that best describes the location of the house.")

# Custom features made by use different fields from the dataset
st.write("Please provide some additional information about the house.")
bedroom_ratio = st.number_input("Individual House Bedroom Ratio in that Area", min_value=0.0, max_value=5.0, value=1.0, help="Enter the ratio of bedrooms to other rooms in an individual house in the area.")
household_rooms = st.number_input("Household Rooms in an Individual House (Estimated)", min_value=0.0, max_value=100.0, value=5.0, help="Enter the estimated number of rooms in an individual house in the area.")

# Convert ocean proximity to one-hot encoding
ocean_proximity_dict = {
    '<1H OCEAN': [1, 0, 0, 0, 0],
    'INLAND': [0, 1, 0, 0, 0],
    'ISLAND': [0, 0, 1, 0, 0],
    'NEAR BAY': [0, 0, 0, 1, 0],
    'NEAR OCEAN': [0, 0, 0, 0, 1]
}
ocean_proximity_encoded = ocean_proximity_dict[ocean_proximity]

# Predict button (using model to predict the price)
if st.button("Predict House Value"):
    features = np.array([[longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, 
                          households, median_income] + ocean_proximity_encoded + [bedroom_ratio, household_rooms]])
    prediction = model.predict(features)
    st.write(f"The predicted house value is: ${prediction[0]:,.2f}")
