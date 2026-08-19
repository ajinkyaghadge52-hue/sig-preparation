"""Bridge 3: Distinguish literal and variable dictionary keys."""


symbol = "AAPL"

literal_key_result = {}
variable_key_result = {}


# Step 1: Add a key literally named "symbol" to literal_key_result.
literal_key_result["symbol"]= 60



# Step 2: Use the value inside the symbol variable as a key in
# variable_key_result.
variable_key_result[symbol]=60


# Step 3: Print both dictionaries and explain why their keys differ.
print(literal_key_result)
print(variable_key_result)