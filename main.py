import sys
from stats import get_num_words, count_characters, get_sorted_list

def get_book_text(file_path):
    file_contents = ''
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    text_list = text.split()
    num_words = get_num_words(text_list)
    character_count_dict = count_characters(text)
    sorted_list = get_sorted_list(character_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for list in sorted_list:
        if list["char"].isalpha():
            print(f"{list['char']}: {list['count']}")
    print("============= END ===============")
main()
