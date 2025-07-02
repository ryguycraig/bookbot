def word_count(text):
   words = text.split()
   return len(words)

def char_count(text):
    counts = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

def sorted_dict(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
