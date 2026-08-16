import pandas as pd

df = pd.read_csv("data/job_runs.csv")


print(df.head())




failed_jobs = df[df["status"] == "FAILED"]

slow_failures = df[
    (df["status"] == "FAILED")
    & (df["duration_seconds"] >= 70)
]

print(slow_failures)
print(failed_jobs)

print(df["job_name"])

print(df[["job_name", "status", "duration_seconds"]])

df["duration_minutes"] = df["duration_seconds"] / 60

print(df["duration_minutes"])


df["duration_minutes"] = df["duration_seconds"] / 60

summary = df[
    ["job_name", "status", "duration_seconds", "duration_minutes"]
]

print(summary)

longest_jobs = df.sort_values(
    "duration_seconds",
    ascending=False,
)

print(longest_jobs[["job_name", "duration_seconds"]])


complete_durations = df.dropna(subset=["duration_seconds"])