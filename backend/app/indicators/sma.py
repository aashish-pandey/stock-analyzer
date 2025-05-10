#calculating the sma
def calculate_sma(df, length=14):
    return df['Close'].rolling(window=length).mean()
    