# Python Foundation Reinforcement

## Containers and access rules

| Container | Purpose | Mutable? | Duplicates? | Access |
|---|---|---:|---:|---|
| List | Ordered sequence | Yes | Yes | Numeric index |
| Tuple | Fixed ordered sequence | No | Yes | Numeric index |
| Set | Unique-value collection | Yes | No | Membership and iteration |
| Dictionary | Key-value mapping | Yes | Keys are unique | Key |

```python
symbols_list[0]
symbols_tuple[0]
"AAPL" in symbols_set
positions_dict["AAPL"]
```

Sets do not support numeric indexing. They are mutable with `add`, `update`, `remove`, `discard`, and `clear`, but their elements must be hashable. `frozenset` is the immutable set form.

## Adding and removing values

```python
values.append(item)        # add to list
values.remove(item)        # remove first matching list value
value = values.pop(index)  # remove list item by index and return it
del values[index]          # remove list item by index

unique.add(item)           # add one unique set value
unique.update(items)       # add several set values
unique.discard(item)       # remove if present without an error

value = mapping.pop(key, None)  # safely remove dictionary key and return value
del mapping[key]                # remove required dictionary key
```

`remove` on a list works by value, `pop` on a list works by index, and dictionary removal works by key. `clear()` empties a mutable container.

## Testing lesson

Correct output does not always prove correct implementation. Accessing `symbols_list[0]` instead of `symbols_tuple[0]` initially produced the same text because both first elements happened to be `AAPL`. Inspect both code and output, and use test data that can expose the difference.

## Next concept

Distinguish function definition from execution, parameters, arguments, and return values.

## Complete container versus current loop item

```python
jobs = [
    {"name": "load_prices", "duration": 12},
    {"name": "validate_trades", "duration": 4},
]

for job in jobs:
    print(job["name"], job["duration"])
```

`jobs` is the complete list. On each iteration, `job` is one dictionary from that list. Therefore, access record fields with `job["name"]`, not `jobs["name"]`. The loop executes once per list item and automatically advances the loop variable to the next record.

## Literal versus variable dictionary keys

Quotation marks mean use the exact text. An unquoted variable name means use the value stored in that variable.

```python
symbol = "AAPL"

literal = {}
literal["symbol"] = 60       # {"symbol": 60}

dynamic = {}
dynamic[symbol] = 60         # {"AAPL": 60}
```

For aggregation, a common flow is:

```text
trade["symbol"] → read the fixed field → store "AAPL" in symbol
result[symbol]   → use "AAPL" as the dynamic output key
```

Memory rule: quotes use exact text; no quotes use the variable's stored value.

## Tuple basics and unpacking

A tuple is a fixed ordered collection. It supports numeric indexing and can group related values such as a symbol and position.

```python
trade_summary = ("AAPL", 60)
symbol, position = trade_summary
```

Tuple unpacking assigns values by position: the first value goes to `symbol` and the second to `position`.

Dictionary `.items()` produces key-value tuples. A loop can unpack each tuple directly:

```python
positions = {"AAPL": 60, "MSFT": 30}

for symbol, position in positions.items():
    print(symbol, position)
```

Here, the loop performs the traversal and each iteration unpacks one `(key, value)` tuple.
