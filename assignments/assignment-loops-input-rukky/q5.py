"""
Q5 — Word Frequency Analyzer

Ask the user for a line of text.
Split it into words, count each word’s frequency, and print the counts.
"""

def main():
    print("=== Word Frequency Analyzer ===")
    text = input("Enter a sentence or paragraph: ").strip()

    if text == "":
        print("You entered nothing.")
        return

    # Convert to lowercase so 'The' and 'the' are counted the same
    words = text.lower().split()

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print("\nWord counts:")
    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
