records = [
    {"id": 1, "status": "SUCCESS"},
    {"id": 2},
    {"id": 3, "status": "FAILED"},
]


# output ["SUCCESS", "UNKNOWN", "FAILED"]

def get_status(records):
    status_summary = []

    for record in records:
        status_summary.append(record.get("status", "UNKNOWN"))

    return status_summary


print(get_status(records))