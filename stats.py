def count_words(sentence):
    num_words = len(sentence.split())
    return num_words


def count_character(text):
    char_dict = {}
    lowercase_text = text.lower()
    for index in range(len(lowercase_text)):
        char = lowercase_text[index]
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def print_report(char_dict):
    restructured_dict = ({"char": char, "num": char_dict[char]} for char in char_dict)
    sorted_dict = sorted(restructured_dict, key=lambda x: x["num"], reverse=True)
    return sorted_dict
