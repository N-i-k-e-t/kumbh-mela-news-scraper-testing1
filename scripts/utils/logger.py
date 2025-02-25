import json
import datetime

LOG_FILE = "logs/logs.json"

# Initialize log structure if not exists
def initialize_log():
    try:
        with open(LOG_FILE, "r") as f:
            json.load(f)  # Check if file is valid JSON
    except (FileNotFoundError, json.JSONDecodeError):
        with open(LOG_FILE, "w") as f:
            json.dump({
                "historical_status": "Not Started",
                "live_status": "Not Started",
                "logs": []
            }, f, indent=4)

# Function to update logs
def update_log(message, historical_status=None, live_status=None):
    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    log_entry = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    data["logs"].append(log_entry)

    if historical_status:
        data["historical_status"] = historical_status
    if live_status:
        data["live_status"] = live_status

    data["logs"] = data["logs"][-100:]  # Limit log size

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Initialize log file
initialize_log()
