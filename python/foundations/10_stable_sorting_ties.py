"""Bridge 10: Handle equal sort keys using stable sorting."""


words = ["pear", "fig", "kiwi", "plum", "apple"]


def get_length(word):

    return len(word)


# Goal: longest words first; equal lengths alphabetically.


# Step 1: Sort words alphabetically and print the result.
sorted_words= sorted(words)
print(sorted_words)

# Step 2: Print every alphabetical word and its length.
for word in words:
    print(word, len(word))

# Step 3: Sort the alphabetical result by length descending.
sorted_by_len= sorted(words, key=get_length, reverse=True)
print(sorted_by_len)

# Step 4: Print the final result and explain the order of equal-length words.

final_sort= sorted(sorted_words, key=get_length, reverse=True)
print(final_sort)
