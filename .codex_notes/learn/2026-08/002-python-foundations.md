# Python Foundations

## Functions and counting matches

A function receives inputs through parameters, processes them, and sends a result back with `return`.

```python
def count_errors(levels):
    error_count = 0

    for level in levels:
        if level == "ERROR":
            error_count += 1

    return error_count
```

The accumulator starts at zero, the loop examines every item, and the condition increments the count only for matches. `return` belongs after the loop; placing it inside would stop the function after the first iteration.

### Trace with intermediate values

For `['INFO', 'ERROR', 'WARN', 'ERROR', 'INFO']`, the counter changes as `0, 1, 1, 2, 2`, so the function returns `2`.

### Complexity

- Time: `O(n)` because every item is inspected once.
- Extra space: `O(1)` because only one counter is stored.

### Interview explanation

> I initialize a counter, iterate through every level, increment only when the level equals `ERROR`, and return after the loop so the entire input is processed.

## Next lesson

Count values by category using a dictionary.

## Filtering records into a list

When several records may match, create a result list and append each complete dictionary.

```python
def find_slow_jobs(jobs, threshold):
    slow_jobs = []

    for job in jobs:
        if job["duration"] > threshold:
            slow_jobs.append(job)

    return slow_jobs
```

A dictionary maps unique keys to values. Reassigning `result["name"]` and `result["duration"]` for every match overwrites the previous record, leaving only the final match. A list stores multiple records, so `.append(job)` preserves every match.

Do not write `result = result.append(item)`: list `.append()` modifies the list and returns `None`.

### Complexity

- Time: `O(n)` because every job is inspected once.
- Extra space: `O(k)` for `k` matching jobs.

### Interview explanation

> I create a separate result list, inspect each job's duration, append the complete job when it exceeds the threshold, and return the result only after checking every job.

## Counting values by category

A dictionary is appropriate when each unique category maps to one count.

```python
def count_levels(levels):
    counts = {}

    for level in levels:
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts
```

The first occurrence creates a key with count `1`; later occurrences increment the existing value. For `['INFO', 'ERROR', 'WARN', 'ERROR', 'INFO', 'ERROR']`, the result is `{'INFO': 2, 'ERROR': 3, 'WARN': 1}`.

### Complexity

- Expected time: `O(n)` because each item uses an average `O(1)` dictionary lookup.
- Extra space: `O(k)` for `k` distinct levels.

### Interview explanation

> I use a dictionary because every distinct level maps naturally to one count. I initialize unseen levels to one and increment levels already present.

## Removing duplicates while preserving order

Use a set for fast membership checks and a list for ordered output.

```python
def remove_duplicates(record_ids):
    seen = set()
    unique_ids = []

    for record_id in record_ids:
        if record_id not in seen:
            seen.add(record_id)
            unique_ids.append(record_id)

    return unique_ids
```

Converting directly to a set removes duplicates but does not provide the required ordered-list result. The two structures have different responsibilities: `seen` answers whether an ID occurred before, while `unique_ids` preserves first appearance order.

### Complexity

- Expected time: `O(n)` because set membership and insertion average `O(1)`.
- Extra space: `O(n)` in the worst case when every ID is unique.

### Interview explanation

> I track encountered IDs in a set for efficient membership checks and append only new IDs to a separate list, preserving first-seen order.

## Normalizing strings

String methods return new strings; they do not modify the original string. Methods can be chained.

```python
def normalize(symbols):
    normalized = []

    for symbol in symbols:
        normalized.append(symbol.strip().upper())

    return normalized
```

`strip()` removes surrounding whitespace and `upper()` standardizes letter case. A misspelled loop variable causes `NameError`; start traceback diagnosis at the final line and compare the referenced name with its definition.

### Complexity

For `n` symbols containing `m` total characters, time and output space are `O(m)` because each character must be processed and new strings are created.

### Interview explanation

> I iterate over the symbols, strip surrounding whitespace, convert each to uppercase, and append the normalized string to a new list so the input remains unchanged.

## List comprehension pattern

A simple transformation loop can be written concisely as:

```python
normalized = [symbol.strip().upper() for symbol in symbols]
```

Use a normal loop when the logic has several steps or the comprehension would be difficult to explain.

## Handling missing dictionary keys

Square-bracket access raises `KeyError` when a key is absent. Use `.get()` with a meaningful default when missing data is expected.

```python
def get_status(records):
    statuses = []

    for record in records:
        statuses.append(record.get("status", "UNKNOWN"))

    return statuses
```

### Interview explanation

> I use square brackets when a key is required and its absence should be an error. When missing data is expected, I use `.get()` with an explicit default such as `UNKNOWN`.

## Handling invalid input with exceptions

Catch the specific error that is expected and allow unrelated bugs to remain visible.

```python
def parse_numbers(values):
    numbers = []

    for value in values:
        try:
            numbers.append(int(value))
        except ValueError:
            continue

    return numbers
```

`continue` skips the remainder of the current loop iteration and proceeds to the next value. A bare `except:` is usually inappropriate because it can hide unexpected programming errors.

### Interview explanation

> I catch only `ValueError` because invalid numeric text is the failure I expect. I skip those records with `continue` while allowing unexpected errors to remain visible.

## Foundation checklist

- Functions, parameters, and return values
- Loops and conditions
- Lists and dictionaries
- Sets and duplicate removal
- String normalization
- Missing dictionary keys
- Targeted exception handling
- Basic time and space complexity

## Combined filtering exercise

```python
def find_long_failures(jobs, minimum_duration):
    result = []

    for job in jobs:
        status = job.get("status")
        duration = job["duration"]

        if status == "FAILED" and duration >= minimum_duration:
            result.append(job["name"])

    return result
```

For a list of dictionaries, `job` is one dictionary on each loop iteration. Use `job.get("status")` for an optional key and `job["name"]` for a required key. The exercise was completed with hints and should be retested independently in the final mock.
