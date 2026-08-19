"""Bridge 1: Understand Python container types and their access rules.

Complete one small section at a time. Predict each result before running it.
"""


symbols_list = ["AAPL", "MSFT", "AAPL"]
symbols_tuple = ("AAPL", "MSFT", "AAPL")
symbols_set = {"AAPL", "MSFT", "AAPL"}
positions_dict = {"AAPL": 60, "MSFT": 30}


# Step 1: Print the type of each container with type(...).
print(type(symbols_list))
print(type(symbols_tuple))
print(type(symbols_set))
print(type(positions_dict))


# Step 2: Print the first item from symbols_list.
print(symbols_list[0])

# Step 3: Print the first item from symbols_tuple.
print(symbols_tuple[0])

# Step 4: Print the AAPL value from positions_dict using its key.
print(positions_dict["AAPL"])

# Step 5: Print every item in symbols_set with a for loop.


for symbol in symbols_set:
    print(symbol)





# Step 6: Access-rule practice

print(symbols_list[1])
print(symbols_tuple[1])
print("GOOGL" in symbols_set)
print(positions_dict["MSFT"])