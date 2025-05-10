import yfinance as yf

def get_data_from_yfinance(symbol, period="6mo", interval="1d"):
    df = yf.download(symbol, period=period, interval=interval, progress=False)

    if df.empty:
        raise ValueError("No data from yfinance.")
    
    return df
