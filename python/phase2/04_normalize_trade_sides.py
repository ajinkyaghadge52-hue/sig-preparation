"""Problem 4: Normalize a list of trade-side values.

Given a list of raw trade-side strings, return a new list containing the
result of normalizing each string.

Use normalize_side() for each item. Do not repeat its normalization logic
inside normalize_sides().

Input:
    [" buy ", "Sell", " hold ", "BUY", ""]

Expected output:
    ["BUY", "SELL", None, "BUY", None]
"""


test_sides = [" buy ", "Sell", " hold ", "BUY", ""]


def normalize_side(side):
    normalized_side = side.strip().upper()

    if normalized_side == "BUY" or normalized_side == "SELL":
        return normalized_side

    return None


def normalize_sides(sides):
    result_list=[]
    for side in sides:
        side= normalize_side(side)
        result_list.append(side)



    return result_list



print(normalize_sides(test_sides))
