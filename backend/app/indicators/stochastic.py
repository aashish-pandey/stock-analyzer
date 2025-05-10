def calculate_stochastic(df, k_period=14):
    lowest_low = df['Low'].rolling(window=k_period).min()
    highest_high = df['High'].rolling(window=k_period).max()

    stoch_k = 100 * ((df['Close'] - lowest_low) / (highest_high - lowest_low))
    return stoch_k