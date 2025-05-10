from app.data_sources.yfinance_loader import get_data_from_yfinance
from app.data_sources.csv_loader import get_data_from_csv

def load_stock_data(symbol, source="yfinance"):
    try:
        if source == "yfinance":
            return get_data_from_yfinance(symbol)
        elif source == "csv":
            return get_data_from_csv(symbol)
        else:
            raise ValueError(f"Unknown data source: {source}")
    except Exception as e:
        print(f"[WARN] Failed to load from {source}: {e}")

        if source != "csv":
            print("[INFO] Trying fallback to CSV...")
            return get_data_from_csv(symbol)
        
        raise RuntimeError("All data sources failed.")