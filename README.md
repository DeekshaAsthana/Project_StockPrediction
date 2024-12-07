# Project_StockPrediction

# 📊 Stock Market Apps

This repository contains two Streamlit applications designed for analyzing and predicting stock market data:

1. **Reddit Stock Market Data Scraper**: Scrape discussions and predictions from Reddit related to the stock market.
2. **Stock Movement Prediction**: Predict the future movement of stock prices based on historical data using a machine learning model.

Both applications provide interactive dashboards and allow users to download various insights, reports, and visualizations.

---

## 1. Reddit Stock Market Data Scraper 🚀

### Overview

The **Reddit Stock Market Data Scraper** fetches the latest posts from a stock market-related subreddit (e.g., `stocks`, `investing`) and performs data analysis and visualizations. You can analyze user discussions, predictions, and insights from the stock market on Reddit.

### Features
- Scrapes stock market-related discussions from Reddit subreddits.
- Provides interactive data insights and visualizations (e.g., top posts by score, comments).
- Allows you to download data as CSV or JSON files.
- Displays metrics like the total number of posts, highest score, and most comments.
- Interactive charts for visualizing post performance.

### Setup Instructions ⚙️

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/stock-market-apps.git
cd stock-market-apps
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Set Up Reddit API Credentials
Create a Reddit application at Reddit Developer Portal and get the Client ID, Client Secret, and User Agent.
Save them in the app as input fields for easy configuration.
4. Run the App
bash
Copy code
streamlit run reddit_scraper_app.py
5. Usage
Enter your Reddit API credentials.
Provide the subreddit name (e.g., stocks) and the number of posts to scrape.
Click Scrape Reddit Data to start fetching data.
View and download the results in various formats (CSV, JSON).
2. Stock Movement Prediction 📈
Overview
The Stock Movement Prediction app predicts stock price movements (up or down) based on historical stock data using a Random Forest Classifier. It fetches stock data, processes it, trains a model, and provides predictions and evaluations.

Features
Fetches historical stock data using Yahoo Finance (yfinance).
Predicts stock price movement (up or down) using a machine learning model.
Provides feature engineering (e.g., moving averages, volatility).
Displays model evaluation metrics: accuracy, precision, and recall.
Visualizes the confusion matrix and feature importance.
Allows you to download predictions, confusion matrix, and feature importance plots.
Setup Instructions ⚙️
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/stock-market-apps.git
cd stock-market-apps
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the App
bash
Copy code
streamlit run stock_prediction_app.py
4. Usage
Enter the stock ticker symbol (e.g., AAPL).
Select the start and end dates for fetching historical data.
Adjust the test size (percentage of data used for testing).
Click Run Model to start fetching data and running predictions.
View model evaluation metrics (accuracy, precision, recall).
Download the classification report, confusion matrix, feature importance plot, and predictions as CSV.
Prerequisites 🛠️
Both applications require the following libraries:

bash
Copy code
pip install streamlit yfinance pandas numpy scikit-learn matplotlib seaborn
You can install all dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
Troubleshooting ⚠️
Reddit Stock Market Data Scraper
Ensure that the Reddit credentials are correctly entered.
Make sure the subreddit exists and has posts within the specified date range.
If the app shows errors related to missing libraries, run the pip install command again.
Stock Movement Prediction
Ensure the stock ticker symbol is valid and available on Yahoo Finance.
If there are errors in fetching or training the model, check the date range and ticker data.
