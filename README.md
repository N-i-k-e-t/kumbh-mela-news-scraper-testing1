# Kumbh Mela News Scraper Dashboard

## 🚀 Overview
This project automates the collection of **Kumbh Mela 2025 news** and provides a **Streamlit-based dashboard** for live tracking.

---

## 📌 Features
- **Automated News Scraping**
- **Google Drive Integration**
- **Real-Time Logging**
- **Live Streamlit Dashboard**
- **GitHub Actions for Automation**

---

## 📂 Project Structure
```
/kumbh-mela-news-scraper-testing
│── .github/workflows/
│   ├── update_logs.yml   # Auto-update logs every 5 min
│
│── scripts/
│   ├── kumbh_mela_news_scraper.py  # Main scraper
│   ├── utils/
│       ├── google_drive_auth.py    # Google Drive authentication
│       ├── logger.py               # Logs scraper activities
│
│── logs/
│   ├── logs.json                   # Live logs storage
│   ├── historical_progress.json     # Tracks historical progress
│   ├── live_progress.json           # Tracks daily collection
│
│── streamlit_dashboard/
│   ├── app.py                       # Streamlit dashboard UI
│
│── reports/
│   ├── kumbh_mela_2025_news_YYYY-MM-DD.txt  # Auto-generated reports
│
│── requirements.txt                  # Python dependencies
│── README.md                          # Project documentation
│── .gitignore                         # Ignore unnecessary files
```

---

## 🚀 Setup & Run
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/N-i-k-e-t/kumbh-mela-news-scraper-testing.git
cd kumbh-mela-news-scraper-testing
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Scraper**
```sh
python scripts/kumbh_mela_news_scraper.py
```

### **4️⃣ Run the Streamlit Dashboard**
```sh
cd streamlit_dashboard
streamlit run app.py
```

---

## 📌 Deployment
### **GitHub Actions (Auto Updates)**
- **Logs update every 5 minutes** via GitHub Actions.
- **Deployed on Streamlit Cloud for public tracking**.

### **Enable GitHub Pages**
- Move `app.py` into `streamlit_dashboard/` folder.
- Deploy via **Streamlit Cloud**.

---

## 🚀 Next Steps
- **Enhance data visualization in Streamlit**.
- **Add NLP sentiment analysis for news data**.

🚀 **Happy Coding!** 🎯
