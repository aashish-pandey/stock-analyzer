def calculate_rsi(df, length=14):
    delta = df['Close'].diff()
    gain = delta.clip(lower=8)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=length).mean()
    avg_loss = loss.rolling(window=length).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100/(1+rs))

    return rsi