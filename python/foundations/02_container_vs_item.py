"""Bridge 2: Distinguish a complete container from one loop item."""


jobs = [
    {"name": "load_prices", "duration": 12},
    {"name": "validate_trades", "duration": 4},
    {"name": "publish_report", "duration": 9},
]


# Step 1: Print the type and value of the complete jobs container.
#print(type(jobs))
#print(jobs)

# Step 2: Loop through jobs. Print the type and value of each current job.
for job in jobs:
    print(type(job))
    print(job)

# Step 3: Inside the loop, print each job's name and duration.
for job in jobs:
    print("Name", job["name"])
    print("Duration", job["duration"])