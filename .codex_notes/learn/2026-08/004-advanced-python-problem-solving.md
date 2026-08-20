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

## Problem 2: Rank positions by absolute exposure

Convert the position dictionary to `(symbol, position)` tuples. Apply the secondary alphabetical rule first, then apply the primary absolute-exposure rule descending. Python's stable sorting preserves alphabetical order when absolute exposures tie.

```python
def rank_positions(positions):
    items = list(positions.items())

    def get_symbol(item):
        symbol, position = item
        return symbol

    def get_absolute_position(item):
        symbol, position = item
        return abs(position)

    alphabetical_items = sorted(items, key=get_symbol)
    ranked_items = sorted(
        alphabetical_items,
        key=get_absolute_position,
        reverse=True,
    )

    return ranked_items
```

The key functions provide temporary comparison values; the returned items retain their original symbol and signed position. The function naturally returns `[]` for an empty dictionary.

### Complexity

- Time: `O(k log k)` for `k` symbols because sorting dominates.
- Extra space: `O(k)` for the tuple lists created by `items()` and `sorted()`.

### Interview explanation

> I convert the mapping into tuples, sort alphabetically to establish the tie order, then stably sort by absolute position descending. Equal exposures retain alphabetical order, and the signed positions remain unchanged in the output.

### Assertions

An assertion compares an actual result with an expected result and raises `AssertionError` when they differ.

```python
assert rank_positions({}) == []

assert rank_positions({"XYZ": -20, "ABC": 20}) == [
    ("ABC", 20),
    ("XYZ", -20),
]
```

Test data is deliberately selected to exercise a rule: empty input checks the edge case, while equal absolute values force alphabetical tie-breaking. `=` assigns; `==` compares.

## Problem 3: Normalize one trade-side value

The function accepts one raw string, removes surrounding spaces, converts it to uppercase, and returns only a supported value.

```python
def normalize_side(side):
    normalized_side = side.strip().upper()

    if normalized_side == "BUY" or normalized_side == "SELL":
        return normalized_side

    return None
```

### One input, one output

`normalize_side(" buy ")` returns `"BUY"`. It does not process the entire list. A separate loop can call this reusable function once for every list item.

Avoid looping over a global list inside this function. Doing that ignores the argument supplied by the caller and makes every function call return the same list.

### Assertions

Assertions call the function with one input and compare its one returned value with the expected value.

```python
assert normalize_side(" buy ") == "BUY"
assert normalize_side(" example ") is None
```

### Complexity

- Time: `O(m)` for a string of length `m`, because normalization reads the string.
- Extra space: `O(m)` for the normalized string.

### Interview explanation

> I normalize one input by stripping surrounding whitespace and converting it to uppercase. I return the normalized value only if it is BUY or SELL; otherwise, I return None. Keeping it as a single-value helper makes it easy to reuse and test.

## Next problem

Process a list of raw trade sides by calling the single-value helper once for each item.

## Problem 4: Normalize a list using a helper

The outer function owns the collection loop. For each raw value, it delegates the single-value work to `normalize_side()` and appends that returned value.

```python
def normalize_sides(sides):
    result_list = []

    for side in sides:
        normalized_side = normalize_side(side)
        result_list.append(normalized_side)

    return result_list
```

The loop must use the `sides` parameter, not the global `test_sides` variable. Otherwise, the function appears correct for the original example but ignores different input supplied by a caller.

Useful independence and edge-case checks:

```python
assert normalize_sides(["SELL"]) == ["SELL"]
assert normalize_sides([]) == []
```

### Complexity

- Time: `O(n * m)` for `n` strings with average length `m`.
- Extra space: `O(n * m)` for the returned normalized strings.

### Interview explanation

> I separate responsibilities: normalize_side handles one string, while normalize_sides loops over the collection and reuses that helper. The function loops over its parameter so it works with any caller-provided list.

## Next problem

Apply the normalization helper to trade dictionaries without duplicating its string-cleaning logic.
