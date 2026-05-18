import pandas as pd
import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine

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
    

def transform_data(raw_data):
    # Transform the raw data into a pandas DataFrame

    if not raw_data:
        return pd.DataFrame()
    
    cleaned_records = []

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for coin_id, values in raw_data.items():
        record = {
            "timestamp": current_time,
            "coin_id": coin_id,
            "price_usd": values.get("usd", None)
        }
        cleaned_records.append(record)

    df = pd.DataFrame(cleaned_records)
    return df


def load_data(df):
    # loads the pandas DataFrame into a SQLite database

    if df is None or df.empty:
        print("No data to load.")
        return
    
    # 1. Create a SQLAlchemy engine to connect to the SQLite database
    engine = create_engine('sqlite:///crypto_prices.db')

    # 2. Load the DataFrame into the database (creates a new table or appends to it)
    df.to_sql(name='prices', con=engine, if_exists='append', index=False)
    print("--- Data Successfully Loaded into SQLite! ---")


if __name__ == "__main__":
    print("--- Starting ETL Pipeline ---")

    raw_prices = fetch_crypto_prices()

    if raw_prices:
        print("1. Extraction Successful!")
        

        df_cleaned = transform_data(raw_prices)
        print("2. Transformation Successful!")
        print(df_cleaned)

        print("3. Attempting to Load Data into Database...")
        try:
            engine = create_engine('sqlite:///crypto_prices.db')
            df_cleaned.to_sql(name='prices', con=engine, if_exists='append', index=False)
            print("--- Data Successfully Loaded into SQLite! ---")
        except Exception as e:
            print(f"--- An error occurred while loading data: {e} ---")
        
    else:
        print("--- FAILURE: Extraction failed, raw_prices is empty. ---")