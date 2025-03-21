def get_num_words(text_list): 
    num_words = len(text_list)
    return num_words
     
def count_characters(text):
    lower_case_text = text.lower()
    word_map = {}

    for letter in lower_case_text:
        if letter not in word_map:
            word_map[letter] = 1
        else:
            word_map[letter] += 1
    return word_map

def sort_on(dict):
    return dict["count"]

def get_sorted_list(character_dict):
    character_list = []
    for character in character_dict:
        tmp_entry = {}
        tmp_entry["char"] = character
        tmp_entry["count"] = character_dict[character]
        character_list.append(tmp_entry)
    character_list.sort(key=sort_on, reverse=True) 
    return character_list

