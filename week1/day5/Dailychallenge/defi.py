

def sort_words():
    """
    Accept a comma-separated sequence of words from the user,
    sort them alphabetically using list comprehension, and print them.
    """
    user_input = input("Enter words separated by commas: ")

    # Split, strip spaces, and sort using list comprehension
    words = [word.strip() for word in user_input.split(",")]
    sorted_words = sorted(words)

    print(",".join(sorted_words))




def longest_word(sentence):
    """
    Find and return the longest word in a sentence.
    If two or more words have the same length, return the first one.
    Punctuation attached to words (apostrophes, commas, periods) counts
    as part of the word.

    Parameters:
        sentence (str): the input sentence

    Returns:
        str: the longest word found
    """
    words = sentence.split()

    # Use list comprehension to get word lengths
    lengths = [len(word) for word in words]

    # Find the index of the maximum length (first occurrence)
    max_index = lengths.index(max(lengths))

    return words[max_index]




def main():
    """Main function to test both challenges."""

    # --- Défi 1 ---
    print("=" * 50)
    print("Défi 1 : Tri")
    print("=" * 50)
    sort_words()

    # --- Défi 2 ---
    print("\n" + "=" * 50)
    print("Défi 2 : Le mot le plus long")
    print("=" * 50)

    print(longest_word("Margaret's toy is a pretty doll."))
    # Expected: Margaret's

    print(longest_word("A thing of beauty is a joy forever."))
    # Expected: forever.

    print(longest_word("Forgetfulness is by all means powerless!"))
    # Expected: Forgetfulness


if __name__ == "__main__":
    main()