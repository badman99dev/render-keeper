import requests
import time

# Yahan apni saari websites ke link daal do
urls = [
    "https://mantraaibot-1.onrender.com/",
    "https://movie-in-db.onrender.com",
    "https://filimizila-direct-movie-link-extractor.onrender.com"
]

print("Starting keep-alive process...")

for url in urls:
    try:
        # Ye wahi kaam karega jo browser karta hai
        response = requests.get(url)
        print(f"Pinged {url} : Status Code {response.status_code}")
    except Exception as e:
        print(f"Error pinging {url}: {e}")

print("All done!")
