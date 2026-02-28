def get_word_count(text):
    words = text.split()
    return len(words)
    
def get_character_count(text):
    char_count = {}
    characters = text.lower()
    for character in characters:
        if character not in char_count:
            char_count[character] = 1
        else:
            char_count[character] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

# def get_sorted_list(text):
#     char_dict = get_character_count(text)
#     items = list(char_dict.items())
    
#     def get_value(kv):
#         return kv[1]
    
#     items.sort(key=get_value, reverse=True)
#     char_list = []
#     for k, v in items:
#         if k.isalpha():
#             char_list.append({k,v})
    
#     for item in char_list:
#         character = item["char"]

def get_sorted_list(num_characters):
    sorted_list = []
    for char, count in num_characters.items():
        # Only include alphabetical characters
        if char.isalpha():
            # The assignment asks for this specific dictionary format
            sorted_list.append({"char": char, "num": count})
    
    # Sort the list using our helper function
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list