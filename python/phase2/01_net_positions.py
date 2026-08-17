trades = [
    {"symbol": "AAPL", "side": "BUY", "quantity": 100},
    {"symbol": "MSFT", "side": "SELL", "quantity": 20},
    {"symbol": "AAPL", "side": "SELL", "quantity": 40},
    {"symbol": "MSFT", "side": "BUY", "quantity": 50},
    {"symbol": "GOOGL", "side": "BUY", "quantity": 10},
]


def calculate_net_positions(trades):
    result = {}

    for trade in trades:
        symbol = trade["symbol"]
        side = trade["side"]
        quantity = trade["quantity"]

        if symbol not in result:
            result[symbol] = 0

        if side == "BUY":
            result[symbol] += quantity
        else:
            result[symbol] -= quantity

    return result


print(calculate_net_positions(trades))