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
    # Write your solution here.
    final=[]
    for symbol, position in positions.items():
        print(symbol, position, abs(position))



print(rank_positions(positions))
