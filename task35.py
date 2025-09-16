def group_by_length(words: list[str]):
    short_words = []
    medium_words = []
    long_words = []

    for w in words:
        if len(w) <= 3:
            short_words.append(w)
        elif len(w) <= 6:
            medium_words.append(w)
        else:
            long_words.append(w)

    return short_words, medium_words, long_words


def main():
    words = input("So'zlarni probel bilan kiriting: ").split()

    short, medium, long = group_by_length(words)

    print("≤3 harfli so'zlar:", short)
    print("4-6 harfli so'zlar:", medium)
    print(">6 harfli so'zlar:", long)


main()
