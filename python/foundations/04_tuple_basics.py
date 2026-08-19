"""Bridge 4: Learn tuple creation, access, and unpacking without sorting."""


trade_summary = ("AAPL", 60)


# Step 1: Print the tuple and its type.
print(trade_summary, type(trade_summary))


# Step 2: Print the first and second values using numeric indexes.
print(trade_summary[0], trade_summary[1])


# Step 3: Unpack the tuple into symbol and position variables.
symbol, position = trade_summary

# Step 4: Print the unpacked variables.
print ("symbol =", symbol, "position =", position)

#Step 5 connect tuples to dictionaries

positions = {
    "AAPL": 60,
    "MSFT": 30,
}

for item in positions.items():
    print(item, type(item))

for name, price in positions.items():
    print("symbol = ", name, "position =", price)
