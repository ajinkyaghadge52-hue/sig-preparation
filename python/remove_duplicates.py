
record_ids = [101, 102, 101, 103, 102, 104]


def remove_duplicates(record_ids):
    seen = set()
    unique_ids = []

    for record_id in record_ids:
        if record_id not in seen:
            seen.add(record_id)
            unique_ids.append(record_id)


    return unique_ids


print(remove_duplicates(record_ids))