import json
import random
import datetime

def generate_log_entry():
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    
    # Randomly select a date in March
    if random.random() < 1/3:
        month = 3
    else:
        month = random.randint(1, 12)
    
    day = random.randint(1, 28)
    year = random.randint(2000, 2022)
    timestamp = datetime.datetime(year, month, day).isoformat()
    
    http_method = random.choice(["GET", "POST", "PUT", "DELETE"])
    url = f"/{random.choice(['home', 'about', 'contact', 'products'])}"
    status_code = random.choice([200, 301, 404, 500])
    user_agent = random.choice(["Mozilla/5.0", "Chrome/91.0.4472.124", "Safari/537.36"])

    log_entry = {
        "ip_address": ip_address,
        "timestamp": timestamp,
        "http_method": http_method,
        "url": url,
        "status_code": status_code,
        "user_agent": user_agent
    }

    return log_entry

log_entries = []
for _ in range(15):
    log_entry = generate_log_entry()
    log_entries.append(log_entry)

log_entries_json = json.dumps(log_entries, indent=4)
print(log_entries_json)