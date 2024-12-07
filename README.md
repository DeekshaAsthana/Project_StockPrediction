
Here's a simplified version of the README.md file:

markdown
Copy code
# Stock Market Apps

This repository contains two Streamlit applications:

1. **Reddit Stock Market Data Scraper**: Scrapes stock market-related discussions from Reddit.
2. **Stock Movement Prediction**: Predicts stock price movements based on historical data.

## 1. Reddit Stock Market Data Scraper

### Features
- Scrapes stock-related discussions from Reddit.
- Visualizes top posts, scores, and comments.
- Download data as CSV or JSON.
- Interactive charts for analysis.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-market-apps.git
   cd stock-market-apps
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up Reddit API credentials:

Create an app on Reddit's developer portal to get the Client ID, Client Secret, and User Agent.
Run the app:

bash
Copy code
streamlit run reddit_scraper_app.py
Enter the subreddit and number of posts, then click Scrape Reddit Data.

2. Stock Movement Prediction
Features
Fetches historical stock data using Yahoo Finance.
Predicts stock movement (up or down) using machine learning.
Displays model metrics (accuracy, precision, recall).
Visualizes confusion matrix and feature importance.
Download results, reports, and plots.
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/stock-market-apps.git
cd stock-market-apps
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run stock_prediction_app.py
Enter the stock ticker (e.g., AAPL), select the start and end dates, and click Run Model.

Prerequisites
Install the required libraries:

bash
Copy code
pip install streamlit yfinance pandas numpy scikit-learn matplotlib seaborn
Troubleshooting
Reddit Scraper: Check Reddit API credentials and subreddit name.
Stock Prediction: Ensure the stock ticker is valid and data is available.
