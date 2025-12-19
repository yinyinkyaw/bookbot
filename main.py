import sys

from stats import count_character, count_words, print_report


def get_book_test(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    content = get_book_test(path_to_book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(content)} total words")
    print("--------- Character Count -------")
    for item in print_report(count_character(content)):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
