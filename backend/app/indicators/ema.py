def calculate_ema(df, length=14):
    return df['Close'].ewm(span=length, adjust=False).mean()