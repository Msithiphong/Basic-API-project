from dotenv import load_dotenv
import requests
import os

load_dotenv()

url = "https://127.0.0.1:8000/generate?prompt=Tell me about Python"
headers = {"x-api-key": os.getenv("API_KEY"), "Content-Type": "application/json"}

response = requests.post(url, headers=headers)
print(response.json())