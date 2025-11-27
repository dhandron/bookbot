def get_num_words(text):
    
    words = text.split(sep=None, maxsplit=-1)
    num_words = len(words)
    
    return num_words

def character_count(text):
    char_count = {}
    if text == "":
        return char_count
    
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1

    return char_count

def sort_on(items):
    return items["num"]

def generate_report(char_count):
    report = []
    for char in char_count:
        report.append({"char": char, "num": char_count[char]})
    report.sort(reverse=True, key=sort_on)
    
    return report