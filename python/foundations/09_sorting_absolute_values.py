"""Bridge 9: Sort signed numbers by absolute value."""


positions = [60, -90, 10, 90]


def get_absolute_value(position):
    return abs(position)


# Step 1: Print every position and its absolute value with a visible loop.
for position in positions:
    print(position, abs(position))

# Step 2: Sort positions by absolute value from smallest to largest.
sorted_pos = sorted(positions, key=get_absolute_value)
print(sorted_pos)

# Step 3: Sort positions by absolute value from largest to smallest.
rev_sorted_pos = sorted(positions, key=get_absolute_value, reverse=True)
print(rev_sorted_pos)

# Step 4: Print both results and the unchanged original list.
print(sorted_pos)
print(rev_sorted_pos)
print(positions)
