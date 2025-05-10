def get_num_of_words(text):
    return len(text.split())

def get_character_count(text):
    data = {}
    for char in text:
        new_char = char.lower()
        if new_char in data:
            data[new_char] += 1
        else:
            data[new_char] = 1
    return data

def get_sorted_list_from_dict(data):
    new_list = []
    for item in data:
        new_list.append({
            "char": item,
            "num": data[item]
        })
    def sort_on(dictionary):
        return dictionary["num"]
    new_list.sort(reverse=True, key=sort_on)
    return new_list


