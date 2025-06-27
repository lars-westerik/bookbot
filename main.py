import sys
from stats import count_words, count_characters, sort_list

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main(path):
    contents = get_book_text(path)
#    print(contents)

    word_count = count_words(contents)
#    print(f"{word_count} words found in the document")

    character_count = count_characters(contents)
#    print(character_count)

    sorted_list = sort_list(character_count)
#    print(sorted_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
main(book_path)