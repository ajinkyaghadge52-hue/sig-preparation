"""Bridge 7: Use one simple named key function for sorting."""


words = ["data", "pipeline", "sql", "python"]


def get_length(word):
    return len(word)


# Step 1: Manually call get_length for one word and print the result.
print(get_length(words[0]))

# Step 2: Use a visible for loop to print every word and get_length(word).
for word in words:
    print(word, "length=", len(word))

# Step 3: Sort words with sorted(words, key=get_length).
sorted_words= sorted(words, key=get_length)
print(sorted_words)


# Step 4: Print the sorted words and the original words.
print(sorted_words, words)