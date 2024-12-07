import streamlit as st
import praw
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv
import time
import plotly.express as px
import re
import json

# Load environment variables from the .env file (optional, if using .env file for credentials)
load_dotenv()

# Custom styles
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
        color: #333333;
    }
    .main-title {
        color: #4CAF50;
        font-family: 'Trebuchet MS', sans-serif;
        text-align: center;
        margin-bottom: 10px;
    }
    .description {
        font-size: 16px;
        color:  #ace0f0;
        line-height: 1.6;
    }
    .sidebar .sidebar-content {
        background-color: #eeeeee;
        padding: 20px;
        border-radius: 8px;
    }
    .metric {
        font-size: 18px;
        font-weight: bold;
        color: #333333;
        text-align: center;
        background-color: #e8f5e9;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown('<h1 class="main-title">📊 Reddit Stock Market Data Scraper</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="description">
    Welcome to the <b>Reddit Stock Market Data Scraper</b>! 🚀  
    Fetch, visualize, and analyze stock market discussions and predictions in a user-friendly interface.  
    Get started by filling in the details in the sidebar!  
    </p>
    """,
    unsafe_allow_html=True,
)

# Sidebar inputs for Reddit credentials
st.sidebar.header("Reddit API Credentials 🔑")
st.sidebar.markdown("---")
client_id = st.sidebar.text_input(
    "Enter Reddit Client ID:",
    help="Your Reddit API client ID. Get it from Reddit's developer portal.",
    value="your_client_id_here",
)
client_secret = st.sidebar.text_input(
    "Enter Reddit Client Secret:",
    help="Your Reddit API client secret. Get it from Reddit's developer portal.",
    value="your_client_secret_here",
    type="password",
)
user_agent = st.sidebar.text_input(
    "Enter Reddit User Agent:",
    help="Your Reddit user agent. Choose a meaningful user agent for the app.",
    value="D_ScraperApp/1.0 by Own-Laugh281",
)

# Sidebar inputs for subreddit and post limit
st.sidebar.header("Subreddit Details 📝")
subreddit_name = st.sidebar.text_input(
    "Enter the Stock Market Subreddit:",
    help="The subreddit related to stock market discussions (e.g., 'stocks', 'investing', etc.)",
    value="stocks",
)
post_limit = st.sidebar.number_input(
    "Number of Posts to Scrape:",
    min_value=10,
    max_value=500,
    step=10,
    value=100,
    help="Specify the number of posts to fetch from the subreddit.",
)

# Scrape button
if st.sidebar.button("Scrape Reddit Data 🚀", help="Click to start scraping data"):
    if subreddit_name and client_id and client_secret and user_agent:
        st.write(f"Fetching posts from Reddit subreddit: **{subreddit_name}**")
        try:
            # Initialize Reddit client with provided credentials
            reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent,
            )

            # Fetch posts from the specified subreddit
            subreddit = reddit.subreddit(subreddit_name)
            submissions = subreddit.new(limit=post_limit)  # Fetch the latest posts

            # Collect post data
            posts = []
            with st.spinner("Scraping data... Please wait!"):
                for submission in submissions:
                    posts.append(
                        {
                            "title": submission.title,
                            "content": submission.selftext,
                            "created_utc": datetime.utcfromtimestamp(
                                submission.created_utc
                            ).strftime("%Y-%m-%d %H:%M:%S"),
                            "score": submission.score,
                            "comments": submission.num_comments,
                            "url": submission.url,
                        }
                    )
                time.sleep(2)  # Simulate loading time

            # Convert to a DataFrame
            if posts:
                df = pd.DataFrame(posts)

                # Data Preprocessing: Clean and preprocess the content
                def clean_text(text):
                    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
                    text = re.sub(r"[^A-Za-z0-9\s]+", "", text)
                    text = text.strip()
                    return text

                df["content_cleaned"] = df["content"].apply(clean_text)

                # Enhanced Visualization Section
                st.markdown('<h2 style="color: #4CAF50;">Data Insights 📊</h2>', unsafe_allow_html=True)
                st.markdown("---")

                st.markdown('<h3 style="color: #ace0f0;">Quick Statistics</h3>', unsafe_allow_html=True)
                col1, col2, col3 = st.columns(3)
                col1.markdown(f'<div class="metric">Total Posts: {len(df)}</div>', unsafe_allow_html=True)
                col2.markdown(f'<div class="metric">Highest Score: {df["score"].max()}</div>', unsafe_allow_html=True)
                col3.markdown(f'<div class="metric">Most Comments: {df["comments"].max()}</div>', unsafe_allow_html=True)

                st.markdown("---")

                # Charts
                st.markdown('<h3 style="color: #ace0f0;">Post Performance Overview</h3>', unsafe_allow_html=True)
                st.markdown("#### Top Posts by Score")
                fig_score = px.bar(
                    df.sort_values(by="score", ascending=False).head(20),
                    x="title",
                    y="score",
                    title="Top 20 Posts by Score",
                    labels={"score": "Scores", "title": "Post Titles"},
                    template="plotly_white",
                    color="score",
                    color_continuous_scale="Viridis",
                    height=400,
                )
                fig_score.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig_score, use_container_width=True)

                st.markdown("#### Top Posts by Comments")
                fig_comments = px.bar(
                    df.sort_values(by="comments", ascending=False).head(20),
                    x="title",
                    y="comments",
                    title="Top 20 Posts by Comments",
                    labels={"comments": "Number of Comments", "title": "Post Titles"},
                    template="plotly_white",
                    color="comments",
                    color_continuous_scale="Cividis",
                    height=400,
                )
                fig_comments.update_layout(xaxis_tickangle=45)
                st.plotly_chart(fig_comments, use_container_width=True)

                # Display Data in Tabs
                st.subheader("Scraped Data 📋")
                tab1, tab2 = st.tabs(["Table View", "Raw JSON"])
                with tab1:
                    st.table(df)
                with tab2:
                    st.json(df.to_dict(orient="records"))

                # Save Data
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                csv_filename = f"{subreddit_name}_reddit_data_{timestamp}.csv"
                json_filename = f"{subreddit_name}_reddit_data_{timestamp}.json"

                os.makedirs("scraped_data", exist_ok=True)
                df.to_csv(csv_filename, index=False)
                with open(json_filename, "w") as f:
                    json.dump(posts, f, indent=4)

                # Download Buttons
                st.download_button(
                    label="Download Data as CSV 📥",
                    data=df.to_csv(index=False).encode("utf-8"),
                    file_name=csv_filename,
                    mime="text/csv",
                )
                st.download_button(
                    label="Download Data as JSON 📥",
                    data=json.dumps(posts, indent=4).encode("utf-8"),
                    file_name=json_filename,
                    mime="application/json",
                )
                st.success(f"✅ Successfully scraped data for subreddit: {subreddit_name}")

            else:
                st.warning("No posts were found for the specified subreddit.")
        except Exception as e:
            st.error(f"Failed to fetch posts: {e}")
    else:
        st.warning("Please provide the Reddit API credentials and subreddit name.")
