def calculate_macd(df, fast=12, slow=26):
    ema_fast = df['Close'].ewm(span=fast, adjust=False).mean()
    ema_slow = df['Close'].ewm(span=slow, adjust=False).mean()

    macd = ema_fast-ema_slow
    return macd