import requests
import time
import datetime
import json
from itertools import cycle
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from scripts.utils.logger import update_log

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.logger import update_log


# Define Tavily API Keys (Use 3 keys for load balancing)
API_KEYS = cycle(["your_api_key_1", "your_api_key_2", "your_api_key_3"])  # Rotate API Keys
MAX_REQUESTS_PER_MINUTE = 70  # API Limit
NEWS_PER_REQUEST = 10  # Number of articles per API call
TOTAL_ARTICLES_PER_DAY = 100  # Target articles per day

# Authenticate Google Drive
def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

drive = authenticate_google_drive()

# Function to fetch news from Tavily API
def fetch_tavily_news(query="Kumbh Mela 2025", num_results=NEWS_PER_REQUEST):
    api_key = next(API_KEYS)  # Rotate API keys
    url = f"https://api.tavily.com/v1/search?query={query}&api_key={api_key}&num_results={num_results}"
    response = requests.get(url)

    if response.status_code == 200:
        update_log(f"Fetched {num_results} articles from Tavily API.")
        return response.json().get("results", [])

    update_log(f"Failed to fetch articles. API response: {response.status_code}")
    return []

# Function to store news articles in a document and upload to Google Drive
def store_news_in_document(news_data, date):
    filename = f"kumbh_mela_2025_news_{date}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"🚀 **Kumbh Mela 2025 News – {date}**\n\n")
        for article in news_data:
            file.write(f"**Headline:** {article['title']}\n")
            file.write(f"**Source:** {article['source']}\n")
            file.write(f"**URL:** {article['url']}\n")
            file.write(f"**Summary:** {article['snippet']}\n\n")
        file.write("---\n\n")

    update_log(f"News saved to: {filename}")

    # Upload to Google Drive
    file_drive = drive.CreateFile({'title': filename})
    file_drive.SetContentFile(filename)
    file_drive.Upload()
    update_log(f"Uploaded {filename} to Google Drive")
    os.remove(filename)  # Delete local file after upload

# Main function to collect and process news
def main():
    today = datetime.date.today()
    update_log(f"🔄 Fetching daily news for {today}...", live_status="In Progress")

    all_news = []
    for _ in range(TOTAL_ARTICLES_PER_DAY // NEWS_PER_REQUEST):
        news_batch = fetch_tavily_news()
        all_news.extend(news_batch)
        time.sleep(60 / MAX_REQUESTS_PER_MINUTE)  # Respect API rate limits

    store_news_in_document(all_news, today)
    update_log("✅ Daily news collection complete.", live_status="Completed")

# Run the script
if __name__ == "__main__":
    main()
