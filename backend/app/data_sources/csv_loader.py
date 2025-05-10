import pandas as pd
import os

def get_data_from_csv(symbol, folder="data"):
    filepath = os.path.join(folder, f"{symbol.upper()}.csv")
    df = pd.read_csv(filepath)

    rename_map = {
        'DATE' : 'Date',
        'OPEN' : 'Open',
        'HIGH' : 'High',
        'LOW' : 'Low',
        'CLOSE' : 'Close',
        'VOLUME' : 'Volume'
    }

    df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns}, inplace=True)

    #set index
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

    required = ['Close', 'High', 'Low', 'Volume']

    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    if df.empty:
        raise ValueError("No data on CSV.")
    
    
    return df