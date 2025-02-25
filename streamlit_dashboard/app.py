import streamlit as st
import json
import time

LOG_FILE = "logs/logs.json"

# Function to load logs
def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        return {"historical_status": "Error", "live_status": "Error", "logs": ["Failed to load logs"]}

# Streamlit UI
def main():
    st.set_page_config(page_title="Kumbh Mela Scraper Dashboard", layout="wide")
    st.title("🚀 Kumbh Mela News Scraper Dashboard")
    
    log_data = load_logs()

    st.header("📊 Scraping Status")
    col1, col2 = st.columns(2)
    col1.metric("Historical Data Collection", log_data["historical_status"])
    col2.metric("Live Data Collection", log_data["live_status"])

    st.header("📜 Logs")
    log_text = "\n".join(log_data["logs"][-20:])
    st.text_area("Latest Logs", log_text, height=300)

    time.sleep(5)
    st.rerun()

if __name__ == "__main__":
    main()
