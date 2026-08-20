"""Bridge 8: Sort simple tuples using one named key function."""


jobs = [
    ("load_prices", 12),
    ("validate_trades", 4),
    ("publish_report", 9),
]


def get_duration(job):
    name, duration = job
    return duration


# Step 1: Manually call get_duration for jobs[0] and print the result.
print(get_duration(jobs[0]))

# Step 2: Use a visible loop to print each tuple and its duration key.
for job in jobs:
    print(job, job[1])

# Step 3: Sort jobs by duration from smallest to largest.

sorted_durations_list= sorted(jobs, key=get_duration)
print(sorted_durations_list)


# Step 4: Print the sorted jobs and the original jobs.
print(sorted_durations_list)
print(jobs)