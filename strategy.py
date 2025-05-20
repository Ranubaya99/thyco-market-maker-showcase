def calculate_optimal_trade(price, inventory):
    # Basic strategy logic
    if price > 3500:
        return {"token_in": "ETH", "token_out": "USDC", "amount_in": 1}
    elif price < 3300:
        return {"token_in": "USDC", "token_out": "ETH", "amount_in": 3400}
    return None
