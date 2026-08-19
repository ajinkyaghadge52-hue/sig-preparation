"""Problem 2: Rank positions by absolute exposure.

Given a dictionary mapping symbols to signed net positions, return a list of
(symbol, position) tuples sorted by:

1. Largest absolute position first.
2. Symbol alphabetically when absolute positions are equal.

Keep the original signed position in the returned tuple.

Example:
    Input:
        {"AAPL": 60, "MSFT": -90, "GOOGL": 10, "TSLA": 90}

    Output:
        [("MSFT", -90), ("TSLA", 90), ("AAPL", 60), ("GOOGL", 10)]

Requirements:
    - Use sorted().
    - Do not implement a sorting algorithm manually.
    - Return a list of tuples.
    - Return [] for an empty dictionary.
"""


positions = {
    "AAPL": 60,
    "MSFT": -90,
    "GOOGL": 10,
    "TSLA": 90,
}


def rank_positions(positions):
    items = list(positions.items())

    def get_symbol(item):
        symbol, position = item
        return symbol

    def get_absolute_position(item):
        symbol, position = item
        return abs(position)

    alphabetical_items = sorted(
        items,
        key=get_symbol,
    )

    ranked_items = sorted(
        alphabetical_items,
        key=get_absolute_position,
        reverse=True,
    )

    return ranked_items

print(rank_positions(positions))
