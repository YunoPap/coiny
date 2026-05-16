import os
import requests
from dotenv import load_dotenv

# 1. Load environment variables from .env file
load_dotenv()

# 2. Get the CoinGecko API key from environment variables
API_KEY = os.getenv('COINGECKO_API_KEY')

if not API_KEY:
    raise ValueError("API key not found. Please set COINGECKO_API_KEY in your .env file.")

# 3. Define the CoinGecko API endpoint
BASE_URL = "https://api.coingecko.com/api/v3"
ENDPOINT = "/simple/price"
HEADERS = {
    "accept": "application/json",
    "X-cg-demo-api-key": API_KEY
}

# 4. Define parameters for the API request
PARAMS = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd",
}

def fetch_crypto_prices():
    try:
        url = f"{BASE_URL}{ENDPOINT}"
        response = requests.get(url, headers=HEADERS, params=PARAMS)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
if __name__ == "__main__":
    prices = fetch_crypto_prices()
    if prices:
        print("--- API Connection Successful ---")
        print(prices)
