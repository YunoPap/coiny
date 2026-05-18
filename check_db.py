import pandas as pd
from sqlalchemy import create_engine

# Connect to your local database file
engine = create_engine("sqlite:///crypto_prices.db")

# Read the entire 'prices' table into a DataFrame
try:
    df = pd.read_sql("SELECT * FROM prices", con=engine)
    print("--- Current Database Contents ---")
    print(df)
except Exception as e:
    print(f"Could not read database. Error: {e}")