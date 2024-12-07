# **Stock Price Forecasting and Data Collection**

This project provides tools for both data collection and stock price forecasting using machine learning, enabling users to analyze historical stock data and predict future prices through an interactive web application.

## **Overview**

The project consists of two core components:
1. **Data Collection**: Retrieve and preprocess historical stock data for any stock symbol.
2. **Price Forecasting**: Use machine learning to predict future stock prices based on the collected data.

### **Features**

1. **Data Collection**
   - Fetch stock data from Yahoo Finance using the `yfinance` library.
   - Specify a stock symbol and date range for data collection.
   - Retrieve daily **Open**, **High**, **Low**, **Close** prices, and trading **Volume**.

2. **Stock Price Forecasting**
   - Build a machine learning model using `RandomForestRegressor` to predict future stock prices.
   - Preprocess and generate features from the data.
   - Evaluate model performance using metrics such as **Mean Squared Error (MSE)**.
   - Visualize predictions through dynamic, interactive plots.

3. **Interactive Web Interface**
   - A user-friendly interface built with `Streamlit` allows users to fetch data and make real-time predictions.

## **Setup Guide**

### **Prerequisites**

Ensure Python 3.7+ is installed on your machine.

### **Installation Steps**


1.**Clone the repository:**
   
   ```bash
   git clone https://github.com/your-username/Project.git
   ```
2.**Navigate to the project directory:**

```bash
cd Project
```
3.**Install the required libraries:**

```bash
pip install -r requirements.txt
```
### **How to Use**


1.**Data Collection**

Fetch historical stock data by running the script:

```bash
python "Data Scraping.py"
```
2.**Stock Price Prediction**

Launch the Streamlit app to forecast stock prices interactively:

```bash
streamlit run "Prediction Model.py"
```
### **Required Libraries**

This project utilizes the following libraries:

yfinance: To fetch historical stock data.

pandas: For data manipulation and preprocessing.

matplotlib: For static visualizations.

scikit-learn: To create and evaluate the prediction model.

streamlit: For building an interactive web application.

plotly: For advanced visualizations.

### **Install all dependencies by running:**

```bash
pip install -r requirements.txt
```
## **How the Application Works**

### **Data Collection**

Fetch stock data for a given stock ticker and date range using yfinance.

The output is a pandas DataFrame containing Open, High, Low, Close, and Volume values.

### **Stock Price Forecasting**

### **Data Preprocessing**

Calculate technical indicators (e.g., 5-day and 10-day moving averages).

Clean and normalize data to ensure compatibility with the model.

### **Model Training**

Split the data into training and testing sets.

Train a RandomForestRegressor model on historical trends.

Evaluate model accuracy using Mean Squared Error (MSE).

### **Forecasting**

Predict future stock prices based on historical data.

Display predictions interactively with visualizations.

### **Notes**

Ensure the stock ticker symbol is valid to avoid errors during data collection.

Predictions are based solely on historical data trends and do not guarantee future stock performance.

Adjust prediction periods as needed to suit forecasting requirements.

### **Acknowledgments**

yfinance: For enabling seamless access to stock data.

scikit-learn: For providing robust machine learning tools.

Streamlit: For simplifying the creation of interactive web applications.
