# q5.py — Word Frequency Analyzer
# What this program does (beginner-friendly):
# 1) Ask for a paragraph of text.
# 2) Normalize it: lowercase + remove simple punctuation.
# 3) Split into words.
# 4) Count how many times each word appears (dictionary).
# 5) Print:
#    - number of UNIQUE words
#    - Top 5 words by frequency (break ties alphabetically).

def clean_text(text: str) -> str:
    """
    Lowercase the text and remove simple punctuation by replacing it with spaces.
    Then collapse extra spaces to single spaces.
    """
    text = text.lower()
    # remove common punctuation; each replaced with a space so words don't stick together
    for ch in ".,!?:;\"'()[]{}-_/\\@#$%^&*+=<>|~`":
        text = text.replace(ch, " ")
    # collapse multiple spaces/newlines/tabs to single spaces
    return " ".join(text.split())

def main():
    # 1) Get a paragraph
    paragraph = input("Paste a short paragraph and press Enter:\n")

    # 2) Clean / normalize
    cleaned = clean_text(paragraph)

    # If user entered nothing meaningful
    if not cleaned:
        print("\nNo words found.")
        return

    # 3) Split into words
    words = cleaned.split()  # e.g., "time flies time" -> ["time", "flies", "time"]

    # 4) Count with a dictionary
    counts = {}  # key: word (str), value: frequency (int)
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # 5) Print stats
    unique_count = len(counts)
    print(f"\nUnique words: {unique_count}")

    # Top 5 by frequency DESC, then by word ASC for ties
    # sorted returns list of (word, freq) tuples
    top5 = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:5]

    print("Top 5 words:")
    for word, freq in top5:
        print(f"{word} \u2192 {freq}")  # pretty arrow: "word → count"

if __name__ == "__main__":
    main()
