import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# Page Configurations
st.set_page_config(page_title="📊 Stock Movement Prediction", layout="wide", initial_sidebar_state="expanded")

# Streamlit App Title
st.markdown("<h1 style='color: #4CAF50; text-align: center;'>📈 Stock Movement Prediction</h1>", unsafe_allow_html=True)

# Sidebar for user inputs
st.sidebar.markdown("<h2 style='color: #ff5733;'>Stock Data Input</h2>", unsafe_allow_html=True)
ticker = st.sidebar.text_input("Enter Stock Ticker Symbol (e.g., AAPL, TSLA):", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-01-01"))
test_size = st.sidebar.slider("Test Size (percentage for testing)", min_value=10, max_value=50, value=20, step=5)
run_model = st.sidebar.button("Run Model")

# Fetch stock data
if ticker and run_model:
    st.markdown(f"<h2 style='color: #4CAF50;'>Fetching Data for {ticker}</h2>", unsafe_allow_html=True)
    try:
        # Load historical stock data using yfinance
        data = yf.download(ticker, start=start_date, end=end_date)
        data.reset_index(inplace=True)

        if data.empty:
            st.error("No data found for the specified ticker and date range.")
        else:
            st.markdown("<h3 style='color: #ff8c00;'>Preview of Stock Data</h3>", unsafe_allow_html=True)
            st.dataframe(data.head(10), use_container_width=True)

            # Feature Engineering
            st.markdown("<h3 style='color: #1f77b4;'>Feature Engineering</h3>", unsafe_allow_html=True)
            data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)  # Upward (1) or downward (0) movement
            data['MA_5'] = data['Close'].rolling(window=5).mean()  # 5-day moving average
            data['MA_10'] = data['Close'].rolling(window=10).mean()  # 10-day moving average
            data['Price_Volatility'] = (data['High'] - data['Low']) / data['Low']  # Price volatility
            data.dropna(inplace=True)  # Drop rows with NaN values
            st.dataframe(data.head(10), use_container_width=True)

            # Define Features and Target
            features = ['Open', 'High', 'Low', 'Volume', 'MA_5', 'MA_10', 'Price_Volatility']
            X = data[features]
            y = data['Target']

            # Split Data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size / 100, random_state=42)

            # Feature Scaling
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            # Train Model
            rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
            rf_model.fit(X_train, y_train)

            # Predictions
            y_pred = rf_model.predict(X_test)

            # Metrics
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)

            # Display Metrics
            st.markdown("<h3 style='color: #4CAF50;'>Model Evaluation Metrics</h3>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            col1.metric("Accuracy", f"{accuracy:.2f}")
            col2.metric("Precision", f"{precision:.2f}")
            col3.metric("Recall", f"{recall:.2f}")

            # Classification Report
            with st.expander("🔍 Classification Report", expanded=True):
                report = classification_report(y_test, y_pred)
                st.text(report)

                # Download Classification Report as text file
                st.download_button(
                    label="Download Classification Report",
                    data=report,
                    file_name="classification_report.txt",
                    mime="text/plain"
                )

            # Confusion Matrix Visualization
            with st.expander("📊 Confusion Matrix", expanded=True):
                conf_matrix = confusion_matrix(y_test, y_pred)
                fig, ax = plt.subplots(figsize=(6, 4))
                sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Down', 'Up'], yticklabels=['Down', 'Up'])
                plt.xlabel("Predicted")
                plt.ylabel("Actual")
                plt.title("Confusion Matrix")
                st.pyplot(fig)

                # Save confusion matrix image for download
                img_buf = BytesIO()
                fig.savefig(img_buf, format="png")
                img_buf.seek(0)
                st.download_button(
                    label="Download Confusion Matrix",
                    data=img_buf,
                    file_name="confusion_matrix.png",
                    mime="image/png"
                )

            # Feature Importance
            with st.expander("🔑 Feature Importance", expanded=True):
                feature_importances = pd.DataFrame({
                    'Feature': features,
                    'Importance': rf_model.feature_importances_
                }).sort_values(by='Importance', ascending=False)
                st.dataframe(feature_importances)

                # Feature Importance Visualization
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.barplot(data=feature_importances, x='Importance', y='Feature', palette='viridis')
                plt.title("Feature Importances")
                st.pyplot(fig)

                # Save feature importance plot for download
                img_buf = BytesIO()
                fig.savefig(img_buf, format="png")
                img_buf.seek(0)
                st.download_button(
                    label="Download Feature Importance Plot",
                    data=img_buf,
                    file_name="feature_importance.png",
                    mime="image/png"
                )

            # Combine data and predictions for download as CSV
            data['Predicted Movement'] = rf_model.predict(scaler.transform(data[features]))
            csv_data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Target', 'Predicted Movement']]
            csv_data = csv_data.dropna()  # Remove any rows with missing data

            # Download button for CSV file
            st.download_button(
                label="Download Data as CSV",
                data=csv_data.to_csv(index=False),
                file_name="stock_data_predictions.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"An error occurred: {e}")
