jobs = [
    {"name": "prices", "status": "FAILED", "duration": 12},
    {"name": "trades", "status": "SUCCESS", "duration": 7},
    {"name": "positions", "status": "FAILED", "duration": 4},
    {"name": "risk", "status": "FAILED", "duration": 15},
    {"name": "archive", "duration": 20},
]



def find_long_failures(jobs, minimum_duration):
    result=[]

    for job in jobs:
        status = job.get("status")
        duration= job.get("duration")

        if(status == "FAILED" and duration >= minimum_duration):
            result.append(job["name"])


    return result


print(find_long_failures(jobs,10))
