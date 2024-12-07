the Reddit Stock Market Data Scraper and the Stock Movement Prediction model:

markdown
Copy code
# Stock Market Data Scraper and Prediction Model

This repository contains two main applications:
1. **Reddit Stock Market Data Scraper**: Scrapes posts from a Reddit subreddit related to stock market discussions and performs data visualization.
2. **Stock Movement Prediction Model**: A predictive model that forecasts the movement of stock prices based on historical data using machine learning.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Reddit Data Scraper](#reddit-data-scraper)
  - [Stock Movement Prediction Model](#stock-movement-prediction-model)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)

## Introduction

### Reddit Stock Market Data Scraper
This app uses the Reddit API to scrape stock market-related discussions from a user-specified subreddit. It cleans and preprocesses the data, then visualizes key statistics such as post score and comment count. The results can be downloaded in both CSV and JSON formats.

### Stock Movement Prediction Model
This app fetches stock data using Yahoo Finance and trains a **Random Forest Classifier** to predict stock price movements. It evaluates the model using metrics such as accuracy, precision, recall, and provides visualizations such as confusion matrix and feature importance.

## Installation

To run the applications, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/stock-market-app.git
   cd stock-market-app
Create a virtual environment (optional but recommended):

'''bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
Install the required dependencies:

'''bash
Copy code
pip install -r requirements.txt
(Optional) If you're using the Reddit Data Scraper, create a .env file with your Reddit API credentials:

'''bash
Copy code
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
USER_AGENT=your_reddit_user_agent
Usage
Reddit Data Scraper
Navigate to the reddit_scraper.py file in the repository.
Open it using Streamlit:
'''bash
Copy code
streamlit run reddit_scraper.py
Fill in the necessary fields in the sidebar:
Reddit Client ID, Client Secret, User Agent: Provide your Reddit API credentials.
Subreddit Name: Enter the name of the subreddit (e.g., stocks, investing).
Number of Posts to Scrape: Choose how many posts you want to scrape.
Click on the "Scrape Reddit Data" button to begin the data scraping process.
The app will display:
Data insights such as total posts, highest score, and most comments.
Visualizations for top posts by score and comments.
The option to download the scraped data in CSV or JSON format.
Stock Movement Prediction Model
Navigate to the stock_prediction.py file in the repository.
Open it using Streamlit:
'''bash
Copy code
streamlit run stock_prediction.py
In the sidebar, input the following:
Stock Ticker Symbol: Enter the stock symbol (e.g., AAPL, TSLA).
Start Date: Select the start date for the historical data.
End Date: Select the end date for the historical data.
Test Size: Select the percentage of data to use for testing.
Click on the "Run Model" button to fetch the stock data and run the predictive model.
The app will display:
A preview of the stock data.
Feature engineering details, such as moving averages and price volatility.
Model evaluation metrics: Accuracy, Precision, Recall.
Confusion matrix and feature importance visualizations.
Downloadable CSV file with the stock data and predicted movements.

Dependencies
The following libraries are required to run the apps:

Streamlit: For building the web interface.
Pandas: For data manipulation.
Plotly: For interactive data visualizations.
Praw: For accessing Reddit's API.
yfinance: For downloading stock data from Yahoo Finance.
Scikit-learn: For training and evaluating the machine learning model.
Matplotlib/Seaborn: For generating plots.
Install the dependencies by running:

'''bash
Copy code
pip install -r requirements.txt
