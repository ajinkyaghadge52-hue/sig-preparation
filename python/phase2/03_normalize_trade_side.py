"""Problem 3: Normalize one raw trade-side string.

Write normalize_side(side) with these rules:

- Remove whitespace from both ends.
- Convert letters to uppercase.
- Return "BUY" for valid buy input.
- Return "SELL" for valid sell input.
- Return None for any unsupported value.

Examples:
    " buy " -> "BUY"
    "Sell"  -> "SELL"
    "HOLD"  -> None
    ""      -> None
"""


test_sides = [" buy ", "Sell", "BUY", " hold ", ""]


test_sides = [" buy ", "Sell", "BUY", " hold ", ""]


def normalize_side(side):
    normalized_side = side.strip().upper()

    if normalized_side == "BUY" or normalized_side == "SELL":
        return normalized_side

    return None


normalized_sides = []

for side in test_sides:
    result = normalize_side(side)
    normalized_sides.append(result)

print(normalized_sides)


assert normalize_side(" buy ") == "BUY"
assert normalize_side("Sell") == "SELL"
assert normalize_side("BUY") == "BUY"
assert normalize_side(" example ") is None
assert normalize_side("  ") is None

print("All assertion tests passed")