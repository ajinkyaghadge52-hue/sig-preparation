def count_errors(levels):
    error_count = 0

    for level in levels:
        if level == "ERROR":
            error_count += 1



    return error_count


levels = ["INFO", "ERROR", "WARN", "ERROR", "INFO"]
print(count_errors(levels))

######### 2  Dictionary code 


jobs = [
    {"name": "load_prices", "duration": 12},
    {"name": "validate_trades", "duration": 4},
    {"name": "publish_report", "duration": 9},
    {"name": "archive_data", "duration": 8},
    {"name": "refresh_positions", "duration": 15},
]

threshold = 8



def find_slow_jobs(jobs, threshold):
    
    final_list = []
    for job in jobs:
        if job['duration']>threshold:
            final_list.append(job)
    
        



    return final_list


print(find_slow_jobs(jobs, threshold))