def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    characters = {}
    for ch in text:
        ch = ch.lower()
        if ch in characters:
            characters[ch] = characters[ch] + 1
        else:
            characters[ch] = 1
    return characters

def sort_on(characters):
    return characters["num"]
    
def chars_dict_to_sorted_list(characters):
    char_list = []
    for ch, count in characters.items():
        char_list.append({"char": ch, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list


