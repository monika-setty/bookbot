def get_num_words(file_content):
    words=file_content.split()
    return len(words)
def get_count_characters(file_content):
    characters_count={}
    characters=list(file_content)
    # print(characters)
    for character in characters:
        lower_case_char=character.lower()
        if lower_case_char in characters_count:
            characters_count[lower_case_char]+=1
        else:
            characters_count[lower_case_char]=1
    return characters_count

def sort_dict(character_count):
    sorted_dict=dict(sorted(character_count.items(), key=lambda item: item[1],reverse=True))
    return sorted_dict

    