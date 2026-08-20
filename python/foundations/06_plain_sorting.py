"""Bridge 6: Use plain sorted() on numbers and strings."""


durations = [90, 10, 60, 30]
symbols = ["TSLA", "AAPL", "MSFT", "GOOGL"]


# Step 1: Print both original lists.
print(durations)
print(symbols)

# Step- 2: Use sorted(durations) and store the returned list.
sorted_durations = sorted(durations)
print(sorted_durations)

# Step 3: Print the sorted durations and the original durations.
print(sorted_durations)
print(durations)

# Step 4: Use sorted(symbols), then print the result.
sorted_symbols=sorted(symbols)
print(sorted_symbols)


desc_durations= sorted(durations, reverse= True)
print(desc_durations)