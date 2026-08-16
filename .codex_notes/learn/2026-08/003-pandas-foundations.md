# Pandas Foundations

## Loading and inspecting a CSV

```python
import pandas as pd

df = pd.read_csv("data/job_runs.csv")
```

A DataFrame is a tabular structure with rows and named columns. Inspect data before analysis:

```python
df.head()          # first five rows
df.shape           # (rows, columns)
df.columns         # column names
df.dtypes          # inferred column types
df.info()          # types and non-null counts
df.isna().sum()    # missing values per column
```

The practice data has 8 rows and 6 columns. `duration_seconds` contains one missing value and is represented as `float64` because ordinary NumPy integer columns cannot represent `NaN`.

### Interview workflow

> I load the CSV, inspect sample rows, confirm its dimensions and schema, review inferred types, and quantify missing values before filtering or aggregating.

## Next lesson

Select columns and create a derived column.

## Filtering rows

```python
failed_jobs = df[df["status"] == "FAILED"]

slow_failures = df[
    (df["status"] == "FAILED")
    & (df["duration_seconds"] >= 70)
]
```

Use `&` for element-wise AND and `|` for element-wise OR in pandas, with each condition enclosed in parentheses. The practice data contains three failed jobs and two failed jobs lasting at least 70 seconds.

### Interview explanation

> I build a boolean mask from the relevant columns and use it to select matching rows. For multiple pandas conditions, I parenthesize each expression and combine them with `&` or `|`.

## Selecting and creating columns

```python
selected = df[["job_name", "status", "duration_seconds"]]
df["duration_minutes"] = df["duration_seconds"] / 60
```

Single brackets with a column name return a Series. Passing a list of names with double brackets returns a DataFrame. Vectorized arithmetic applies to the complete column and preserves missing values as `NaN`.

### Interview explanation

> I select multiple columns with a list of column names and create derived columns using vectorized operations rather than row-by-row Python loops.

## Sorting rows

```python
longest_jobs = df.sort_values("duration_seconds", ascending=False)
```

`sort_values()` returns a new sorted DataFrame by default. Supply a list of columns and a corresponding list of ascending flags for multi-column sorting. Missing values appear last by default.

### Interview explanation

> I sort with `sort_values`, explicitly state descending order when needed, and retain the original DataFrame unless mutation is intentional.

## Handling missing values

```python
complete = df.dropna(subset=["duration_seconds"])
median_duration = df["duration_seconds"].median()
df["duration_filled"] = df["duration_seconds"].fillna(median_duration)
```

Use `dropna()` when a row cannot support the analysis without a required value. Use `fillna()` only when the replacement has a defensible meaning. Preserve raw data by creating a separate filled column when auditability matters; do not assume missing numeric data means zero.

### Interview explanation

> I quantify missing values first, then choose dropping or imputation based on the analysis and business meaning. I often preserve the raw column and create a separate imputed column.

## Grouping and aggregation

Think of `groupby` as putting rows into category buckets, then calculating one result for each bucket.

```python
df.groupby("team")["records_processed"].sum()
```

This groups rows into team buckets, selects `records_processed`, and adds the values within each bucket. The practice totals are market data 2900, operations 2950, risk 1300, and trading 2000.

```python
df.groupby("team")["duration_seconds"].mean()
df.groupby("status").size()
```

`size()` counts rows, while `count()` on a specific column counts non-missing values in that column.

For several named metrics:

```python
team_summary = df.groupby("team", as_index=False).agg(
    run_count=("run_id", "count"),
    average_duration=("duration_seconds", "mean"),
    total_records=("records_processed", "sum"),
)
```

### Memory rule

```text
groupby = make buckets
sum / mean / count = calculate something for each bucket
```

### Interview explanation

> I group rows by the relevant category and apply aggregations such as sum, mean, or count to each group. I use `size` for row counts and `count` for non-null values in a selected column.

## Timed analysis result

The combined exercise loaded and inspected the CSV, filtered failed rows, grouped them by team, calculated failure counts, average duration, and total records, then sorted totals descending. The key correction was to filter first; grouping the full DataFrame would mix successful and failed runs.

### Reliable analysis order

```text
load → inspect → filter → group → aggregate → sort → present
```
