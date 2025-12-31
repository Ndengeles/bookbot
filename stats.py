def count_words(text):
    return len(text.split())


def count_chars(text):
    """Return a dict mapping each lowercase character to its frequency in text.

    Counts all characters (letters, digits, punctuation, whitespace, etc.) and
    treats characters case-insensitively by converting to lowercase.
    """
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def sort_char_counts(char_counts):   
    items = [{"char": c, "num": n} for c, n in char_counts.items()]

    def _get_num(d):
        return d["num"]

    items.sort(key=_get_num, reverse=True)
    return items
