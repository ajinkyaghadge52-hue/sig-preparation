"""Bridge 5: Function definition, execution, parameters, and returns."""


def describe_job(name, duration):
    message = f"{name} took {duration} seconds"
    return message


# Step 1: Predict whether defining describe_job prints anything.
describe_job("load_prices", 12)

# Step 2: Call describe_job with "load_prices" and 12. Store its return value.
result = describe_job("load_prices", 12)
#print(result)

# Step 3: Print the stored return value.
print(result)

# Step 4: Call the same function with a different name and duration.
result2 = describe_job("stock prices", 15)
print(result2)

