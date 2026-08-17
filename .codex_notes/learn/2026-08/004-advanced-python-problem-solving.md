# Advanced Python Problem Solving

## Problem 1: Net positions by symbol

Given trade dictionaries, add BUY quantities and subtract SELL quantities for each symbol.

```python
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
```

### Data-structure model

`trades` is a list; each `trade` produced by the loop is one dictionary. The output has a different shape: actual symbols become keys and accumulated positions become values.

```text
trade["quantity"] → read from the current input record
result[symbol]    → update the accumulated output for that symbol
result["symbol"]  → literal key named "symbol"; not appropriate here
```

Initialize a new symbol to zero, then independently decide whether to add or subtract. No `else` is needed for initialization because an existing symbol should retain its current value.

### Complexity

- Time: `O(n)` for `n` trades.
- Extra space: `O(k)` for `k` distinct symbols.

### Interview explanation

> I use a dictionary keyed by symbol. For each trade, I initialize an unseen symbol to zero, add buys, and subtract sells. This processes every trade once and stores one value per distinct symbol.

## Next problem

Sort positions using a custom ranking rule.
