# coiny

A small Python project for working with cryptocurrency data.

## Setup

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your CoinGecko API key:
   ```text
   COINGECKO_API_KEY=your_api_key_here
   ```

## Usage

- `main.py` is currently a placeholder that imports `pandas`.
- `pipeline.py` fetches crypto prices from the CoinGecko API.

Run it with:
```bash
python pipeline.py
```

## Notes

- The virtual environment is stored in `.venv/` and is excluded from git by `.gitignore`.
- If you want to add more dependencies, update `requirements.txt` and rerun:
  ```bash
  pip install -r requirements.txt
  ```
