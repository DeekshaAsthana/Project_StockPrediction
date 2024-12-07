Stock Price Forecasting and Data Collection
This project comprises two distinct sections:

Data Collection: Retrieves stock market data for any given stock symbol.
Price Forecasting: Uses machine learning algorithms to predict future stock prices based on historical stock data.
Overview
This project allows you to:

Collect Stock Data: Fetch historical stock data from Yahoo Finance using the yfinance library.
Data Preprocessing: Clean and prepare the data for use in the machine learning model.
Predict Stock Prices: Implement a machine learning model, specifically RandomForestRegressor, to predict future stock prices.
Interactive Web Interface: Build an interactive app with Streamlit to make real-time predictions based on the selected stock.
Key Features
1. Data Collection
Collects stock data from Yahoo Finance for any stock symbol.
The user can specify a date range for which the data should be scraped.
Stock data includes daily Open, High, Low, Close prices, and Volume.
2. Stock Price Forecasting
A machine learning model based on RandomForestRegressor is built to predict future stock prices.
Data is preprocessed, and features are generated before splitting the data into training and testing datasets.
The performance of the model is evaluated using Mean Squared Error (MSE).
The model forecasts stock prices for future dates and visualizes the predictions.
Setup Guide
Prerequisites
Make sure you have Python 3.7+ installed on your machine.

Installation Steps
To set up the project locally, follow these steps:

Clone the Repository:

git clone https://github.com/your-username/Project.git
Navigate to the Project Directory:

cd Project
Install Required Packages:

Install the necessary libraries by running:


pip install -r requirements.txt
Running the Application
1. Data Collection
To fetch stock market data for a specific ticker symbol, run:


python "Data Scraping.py"
2. Stock Price Prediction
To run the machine learning model and launch the interactive Streamlit app, execute:


streamlit run "Prediction Model.py"
Required Libraries
This project uses the following libraries:

yfinance: To fetch stock data from Yahoo Finance.
pandas: For data manipulation and preprocessing.
matplotlib: To generate plots and visualizations.
scikit-learn: For creating and evaluating machine learning models.
streamlit: To build a user-friendly web interface.
plotly: For interactive and dynamic visualizations.
Install all the required libraries at once by running:


pip install -r requirements.txt
How the Application Works
Data Collection
The stock data is fetched using the yfinance library, where you specify the stock ticker and the date range.
The data is returned as a pandas DataFrame, which contains the stock's daily Open, High, Low, Close, and Volume information.
Stock Price Prediction
Data Preprocessing
Historical stock data is used to calculate technical indicators like moving averages (e.g., 5-day and 10-day averages).
The data is cleaned and normalized before feeding it into the prediction model.
Model Training
The data is split into a training set and a testing set to train the RandomForestRegressor model.
The model is trained using historical data to learn patterns in the stock prices.
The model is then tested and evaluated using Mean Squared Error (MSE) to measure its accuracy.
Price Forecasting
After training, the model predicts future stock prices based on historical trends.
The results are displayed in an interactive visualization that allows the user to view the predicted stock prices over time.
Notes
Always verify that the stock ticker entered is correct to avoid errors in data fetching.
The model’s predictions are based solely on historical data and market trends, and they do not guarantee future stock performance.
You can adjust the prediction period to forecast stock prices for a specified number of days.
Acknowledgments
Thanks to yfinance for providing easy access to stock market data.
Thanks to scikit-learn for powerful machine learning tools to create predictive models.
Thanks to Streamlit for enabling the development of interactive web applications.
