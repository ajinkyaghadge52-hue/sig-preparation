levels = ["INFO", "ERROR", "WARN", "ERROR", "INFO", "ERROR"]



def count_levels(levels):
    counts ={}
    for level in levels:
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1






    return counts


result=count_levels(levels)


print(result)