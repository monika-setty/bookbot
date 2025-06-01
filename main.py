import stats
import sys
def get_book_text(file_Path):
    with open(file_Path) as f:
        file_content=f.read()
        return str(file_content)
def main():
    # s="monika j d f f"
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_content=get_book_text(sys.argv[1])
        no_of_words=stats.get_num_words(file_content)
        print(f"{no_of_words} words found in the document")
        characters_count=stats.get_count_characters(file_content)
        print(characters_count)
        print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\n Found {no_of_words} total words\n--------- Character Count -------")
        Character_count_sorted=stats.sort_dict(characters_count)
        for character in Character_count_sorted:
            if character.isalpha():
                print(f"{character}: {Character_count_sorted[character]}")
if __name__=="__main__":
    main()