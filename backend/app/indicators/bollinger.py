def calculate_bollinger(df, length=20, num_std=2):
    sma = df['Close'].rolling(window=length).mean()
    std = df['Close'].rolling(window=length).std()

    upper_band = sma + (num_std * std)
    lower_band = sma - (num_std * std)

    return upper_band, lower_band