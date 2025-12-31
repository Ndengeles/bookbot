import sys
from stats import count_words, count_chars, sort_char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_counts = count_chars(text)
    sorted_char_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        ch = entry["char"]
        num = entry["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============") 
if __name__ == "__main__":
    main()
