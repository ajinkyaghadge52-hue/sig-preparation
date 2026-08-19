# Python Data Analysis and Data Engineering Mastery Plan

## Objective

Build Python capability from first principles through practical data-analysis and data-engineering work. Treat prior exposure as useful but do not assume mastery. Fast-track concepts that pass a short independent check and slow down wherever the mental model is unclear.

This roadmap is the canonical sequence for the repository. It is intended to become a one-stop Python preparation system containing exercises, corrected solutions, mistake patterns, complexity notes, and realistic projects.

## Personalized entry point

Do not restart every completed exercise. Use a bridge sequence based on demonstrated performance.

### Demonstrated foundations

- Write and call basic functions.
- Use `for` loops and `if` conditions.
- Count, filter, and accumulate values with guidance.
- Use lists, dictionaries, and sets in straightforward cases.
- Normalize strings and handle targeted exceptions.
- Load, inspect, filter, sort, fill, group, and aggregate pandas data.
- Read tracebacks and correct concrete runtime errors.

These topics receive short retrieval checks rather than full reteaching unless a check fails.

### Concepts requiring reinforcement

- Distinguishing a container from one item inside it.
- Distinguishing literal dictionary keys from variable keys.
- Lists versus tuples versus dictionaries and their access rules.
- Tuple creation, indexing, and unpacking.
- Function definition versus execution and how arguments are passed.
- Built-in functions that call a supplied function, such as `sorted(key=...)`.
- Predicting state across loop iterations without executing the code.
- Independently translating a word problem into an output data structure.

### Bridge sequence

1. Container map: list, tuple, dictionary, and set using the same small dataset.
2. One-item versus whole-container tracing inside a loop.
3. Literal values versus variables, especially dictionary keys.
4. Tuple construction and unpacking without sorting.
5. Function calls, parameters, and returns using manually called helpers.
6. Plain `sorted()` on numbers and strings.
7. `sorted(..., reverse=True)`.
8. One named key function on a list of words.
9. One named key function on simple tuples.
10. Resume `02_rank_positions.py` with printed intermediate keys.

Each bridge step gets its own file under `python/foundations/`. After the bridge, continue Stage 6 problem-solving while revisiting later roadmap stages in order.

### Advancement rule

Advance when the learner can predict output, write the small example independently, and explain why it works. If only syntax is forgotten, provide a syntax reminder and continue. If the mental model is unclear, split the concept again rather than adding more syntax.

## Teaching contract

For every concept:

1. Explain one idea in plain language.
2. Show its input, output, and purpose.
3. Trace concrete intermediate values.
4. Give one tiny isolated exercise.
5. Let the learner attempt it before showing a solution.
6. Run the saved code and explain the first failing line simply.
7. Test a normal case and at least one edge case.
8. Record only the durable revision points after completion.
9. Combine concepts only after their prerequisites pass independently.
10. Introduce concise syntax such as lambdas and comprehensions only after the verbose form is understood.

## Repository organization

```text
python/
  foundations/       # isolated language concepts
  problem_solving/   # progressive coding problems
  data_files/        # text, CSV, and JSON exercises
  testing/           # tests and debugging exercises
  projects/          # integrated DA/DE projects
pandas/              # pandas-specific exercises
data/                # small, known practice datasets
.codex_notes/learn/  # concise completed learning references
PROGRESS.md           # canonical completion and mistake tracker
```

Use one file per concept or problem. Do not accumulate unrelated exercises in one script.

## Stage 0: Execution foundations

- Python files versus the REPL
- Interpreter and virtual-environment selection
- Statements, expressions, output, and comments
- Reading tracebacks from the final line upward
- Values, types, variables, and assignment
- Using `type()` and simple intermediate prints

Mastery check: independently run a file, inspect types, and explain a simple traceback.

## Stage 1: Scalar values and operators

- Integers, floats, booleans, strings, and `None`
- Arithmetic and comparison operators
- Boolean logic: `and`, `or`, and `not`
- Truthiness
- String indexing, slicing, formatting, and core methods
- Converting between compatible types

Mastery check: normalize and validate individual text and numeric values.

## Stage 2: Containers, one at a time

### Lists

- Ordered collection model
- Numeric indexing and slicing
- Mutation, `append`, and return-value behavior
- Iteration and membership

### Tuples

- Fixed ordered collection model
- Indexing and unpacking
- Why dictionary `.items()` yields key-value tuples
- Returning several related values

### Dictionaries

- Key-value model
- Literal keys versus variable keys
- Required access with `[]` versus optional access with `.get()`
- Iterating keys, values, and items
- Aggregation by category

### Sets

- Uniqueness and membership
- Duplicate removal
- Set operations
- Preserving order with a separate list

Mastery check: choose and explain the correct container without mixing their access rules.

## Stage 3: Control flow

- `if`, `elif`, and `else`
- Independent `if` statements versus one conditional chain
- `for` loops and loop variables
- `while` loops and termination
- `break`, `continue`, and nested flow
- Tracing state across iterations

Mastery check: trace every iteration and predict output before execution.

## Stage 4: Functions

- Parameters, arguments, local variables, and return values
- Function definition versus function call
- Default and keyword arguments
- Scope and avoiding unnecessary global state
- Returning lists, dictionaries, and tuples
- Pure functions and input mutation

Mastery check: implement and explain short functions without copying.

## Stage 5: Errors, validation, and debugging

- `SyntaxError`, `NameError`, `TypeError`, `KeyError`, `IndexError`, and `ValueError`
- Targeted `try` / `except` / `else` / `finally`
- Raising meaningful exceptions
- Input validation and edge cases
- Assertions and debug prints

Mastery check: identify error type, failing line, cause, and minimal correction.

## Stage 6: Core problem-solving patterns

- Counting and accumulation
- Filtering and transformation
- Min/max and running best
- Frequency dictionaries
- Deduplication
- Grouping records
- Two-pointer and sliding-window foundations
- Stack and queue foundations
- Sorting only after iteration, tuples, and functions are secure
- Custom sort keys, stability, and tie-breaking

Mastery check: state inputs, outputs, data structure, algorithm, edge cases, and complexity before coding.

## Stage 7: Python standard library for data work

- `collections.Counter`, `defaultdict`, and `deque`
- `datetime` and time-zone-aware timestamps
- `pathlib` for paths
- `re` for controlled text patterns
- `math`, `statistics`, and `decimal`
- `itertools` for composable iteration

Mastery check: solve a realistic task first with core Python, then recognize the suitable standard-library tool.

## Stage 8: Files and serialization

- Context managers and `with open(...)`
- Text files and line-by-line processing
- CSV reading and writing
- JSON objects and arrays
- Encoding, delimiters, malformed rows, and missing fields
- Streaming large files rather than loading everything

Mastery check: build a safe file-to-summary transformation with validation and clear error reporting.

## Stage 9: Iteration and memory efficiency

- Iterable versus iterator
- `iter()` and `next()`
- Generator functions and `yield`
- Generator expressions
- Lazy processing and chunking
- Time and space tradeoffs

Mastery check: process a large conceptual dataset without constructing unnecessary full-size intermediate lists.

## Stage 10: Testing, typing, and maintainability

- Test cases and boundary cases
- `pytest` fundamentals
- Fixtures and parameterized tests
- Type hints and common container annotations
- Docstrings and readable naming
- Logging instead of uncontrolled prints
- Small modules and separation of concerns

Mastery check: implement a function and an accompanying test suite that covers normal, empty, invalid, and boundary inputs.

## Stage 11: NumPy and pandas for data analysis

- NumPy arrays, shapes, dtypes, indexing, masks, and vectorization
- DataFrame and Series mental models
- Loading and inspecting data
- Selecting, filtering, sorting, and assigning
- Missing values and type conversion
- Grouping and aggregation
- Merging, joining, concatenating, and reshaping
- Datetime operations
- Duplicate handling and data validation
- Avoiding row-by-row loops when vectorization fits
- Performance and memory inspection

Mastery check: independently explore an unfamiliar dataset and produce a defensible analysis with validation.

## Stage 12: Data-engineering Python

- Extract-transform-load structure
- Schema validation and normalization
- Idempotency and safe reruns
- Batch and chunk processing
- Checkpoints and failure recovery
- Structured logging and metrics
- Configuration and environment variables
- API pagination and retries
- Database access and transactions
- File partitioning and naming conventions
- Data-quality checks

Mastery check: build a small repeatable pipeline that can fail safely, rerun safely, and explain its operational behavior.

## Stage 13: Advanced Python

- Classes and data classes
- Composition and useful object boundaries
- Decorators after functions are secure
- Context-manager implementation
- Concurrency concepts: threads, processes, and async I/O
- Packaging and dependency management
- Profiling and optimization

Mastery check: select advanced features because they solve a concrete problem, not merely to make code sophisticated.

## Integrated projects

1. Log-quality analyzer using streaming text processing.
2. Trade and position reconciler using core Python and CSV/JSON.
3. Pandas operations dashboard with data-quality reporting.
4. Idempotent batch ETL pipeline with logging, validation, and tests.
5. Timed interview pack containing Python, pandas, debugging, and reasoning exercises.

## Mastery gates

A topic is complete only when the learner can:

- Explain it without reading the solution.
- Predict intermediate values.
- Implement the basic pattern independently.
- Debug a deliberately broken version.
- Handle normal and edge cases.
- State time and space complexity where relevant.
- Apply it in a realistic data scenario.

## Immediate sequence

Follow the personalized bridge sequence above. Begin with one shared dataset represented as a list, tuple, dictionary, and set, then practise accessing the whole container versus one item. Return to `02_rank_positions.py` only after the bridge checks pass.
