# task5.py
# Approach:
# 1. Ask the user for a short paragraph.
# 2. Clean text by converting to lowercase and removing punctuation (.,!?).
# 3. Split text into words.
# 4. Build a dictionary mapping each word to its frequency using loops.
# 5. Print number of unique words.
# 6. Print the top 5 most frequent words (ties broken alphabetically).

# Step 1: Input
text = input("Paste a short paragraph: ")

# Step 2: Clean text
cleaned = text.lower()
for p in ".,!?":
    cleaned = cleaned.replace(p, "")

# Step 3: Split into words
words = cleaned.split()

# Step 4: Count frequencies
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Step 5: Number of unique words
unique_count = len(freq)
print(f"\nUnique words used: {unique_count}")

# Step 6: Sort and print top 5
# Sorting by (-count, word) ensures high frequency first, ties alphabetically
sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

print("\nTop 5 most frequent words:")
for word, count in sorted_words[:5]:
    print(f"{word} → {count}")
