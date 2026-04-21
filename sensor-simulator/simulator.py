import time
import random
import requests

BACKEND_URL = "http://backend:5000/api/readings"

while True:
    data = {
        "temperature": round(random.uniform(20.0, 28.0), 1),
        "humidity": random.randint(30, 60),
        "motion": random.choice([True, False])
    }

    try:
        response = requests.post(BACKEND_URL, json=data)
        print("Sent:", data, "Status:", response.status_code)
    except Exception as error:
        print("Error sending data:", error)

    time.sleep(5)
