# California-house-price-predictor
This project is a house price prediction tool for the state of California. Utilizing a regressor model, it trains and predicts house values based on various factors. Additionally, I have developed a simple web application that allows users to input values and obtain an estimated house price.
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Data Analysis](#data-analysis)
- [Contributing](#contributing)
- [License](#license)

## Overview

The California House Price Predictor is a web application that estimates the value of a house based on user-provided features. The model was trained on historical housing data and incorporates various features to make accurate predictions.

## Disclaimer

Please note that this model has an accuracy of 81% and should be used with caution. It is intended for educational purposes and should not be relied upon for making financial decisions.


## Features

- **Web Application**: A user-friendly interface to input house features and get price predictions.
- **Model Training**: Detailed notebooks showcasing model training, and saving the model.
- **Data Analysis**: Exploratory data analysis to understand the housing market trends in California and showcasing data preprocessing, and feature engineering.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/california-house-price-predictor.git
    ```

2. Navigate to the project directory:
    ```
    cd california-house-price-predictor
    ```

3. Install the required dependencies:
    ```
    pip3 install "library name"
    ```



## Usage

1. Run the file app.py to open the web app.
2. Input the house features in the form provided.
3. Click the "Predict" button to get the estimated house value.

## Model Training

The `model.ipynb` notebook contains the following steps:

1. **Data Loading and Preprocessing**:
    - Handling missing values, feature scaling, and encoding categorical variables.
    - Analysis of different features and their correlation with the target value (house value).
  
2. **Feature Engineering**:
    - Creating new features like `bedroom_ratio` and `household_rooms` to enhance model performance.

3. **Model Training**:
    - Training and evaluating various machine learning models (e.g., Linear Regression, Decision Tree, Random Forest).

4. **Model Selection and Saving**:
    - Selecting the best-performing model and saving it using `pickle` for deployment in the web application.

## Data Analysis

The `priceanalysis.ipynb` notebook includes:

1. **Exploratory Data Analysis (EDA)**:
    - Understanding the distribution and trends of house prices in California.

2. **Visualization**:
    - Creating plots and graphs to visualize the relationships between features and house prices.

3. **Insights and Conclusion**:
    - Drawing key insights and conclusions from the analysis to better understand the housing market.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
