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

Apply the completed sorting bridge to the paused position-ranking problem.

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

## Function definition, calls, and return values

`def` creates a function but does not execute its body. A function call supplies arguments to its parameters and executes the stored instructions.

```python
def describe_job(name, duration):
    message = f"{name} took {duration} seconds"
    return message

result = describe_job("load_prices", 12)
print(result)
```

`name` and `duration` are parameters; `"load_prices"` and `12` are arguments. `return` sends a value back to the caller. Without an explicit return, Python returns `None`.

```python
print(describe_job("load_prices", 12))
```

This prints a returned value directly. A bare function call in a script executes the function but does not display its return value. Prefer returning data from processing functions so callers can store, print, test, or transform it.

## Plain sorting

`sorted()` traverses an iterable internally, returns a new list, and leaves the original collection unchanged.

```python
durations = [90, 10, 60, 30]

ascending = sorted(durations)                 # [10, 30, 60, 90]
descending = sorted(durations, reverse=True)  # [90, 60, 30, 10]
```

Strings sort alphabetically by default. `reverse=False` is the default ascending direction; `reverse=True` requests descending order.

## Sorting with a named key function

A key function returns the temporary comparison value for one item. `sorted()` internally calls it for every item but returns the original items in the resulting order.

```python
words = ["data", "pipeline", "sql", "python"]

def get_length(word):
    return len(word)

sorted_words = sorted(words, key=get_length)
```

The helper returns `4`, `8`, `3`, and `6`; the output is `['sql', 'data', 'python', 'pipeline']`. The original list is unchanged. Passing `key=get_length` gives the function itself to `sorted`; writing `get_length(word)` manually calls it for one word.

## Sorting tuples by one field

```python
jobs = [
    ("load_prices", 12),
    ("validate_trades", 4),
    ("publish_report", 9),
]

def get_duration(job):
    name, duration = job
    return duration

sorted_jobs = sorted(jobs, key=get_duration)
```

`sorted()` receives the complete list and internally passes one tuple at a time to `get_duration`. The helper returns `12`, `4`, and `9` as comparison keys, while the output retains the original tuples in the corresponding order. No external loop or `.append()` is needed.

## Sorting by absolute value

```python
positions = [60, -90, 10, 90]

def get_absolute_value(position):
    return abs(position)

ascending = sorted(positions, key=get_absolute_value)
descending = sorted(positions, key=get_absolute_value, reverse=True)
```

The helper supplies `60`, `90`, `10`, and `90` for comparison, but the output retains the original signed values. Ascending produces `[10, 60, -90, 90]`; descending produces `[-90, 90, 60, 10]`. Equal keys retain their existing relative order because Python sorting is stable.

## Stable sorting and tie-breakers

For multiple rules with stable sorting, apply the secondary rule first and the primary rule second.

```python
alphabetical_words = sorted(words)
final_words = sorted(
    alphabetical_words,
    key=get_length,
    reverse=True,
)
```

The second sort ranks lengths descending. Equal-length words preserve their existing alphabetical order. This is sequential sorting, not recursion.

```text
secondary rule first → alphabetical
primary rule second  → length descending
```
