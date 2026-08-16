import pandas as pd


df = pd.read_csv("data/job_runs.csv")

print(df.shape)
print(df.isna().sum())


print(df.head())

failed_jobs = df[df["status"]=="FAILED"]
print(failed_jobs)


failure_summary= failed_jobs.groupby("team", as_index=False).agg(

    failed_run_count=("status","count"),
    duration_scronds= ("duration_seconds","mean"),
    records_processed= ("records_processed","sum")
)

failure_summary = failure_summary.sort_values(
    "records_processed",
    ascending=False
)

print(failure_summary)