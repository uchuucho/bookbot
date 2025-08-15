def get_num_words(text) :
    return len(text.split())

def count_letters(text) :
    letter = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            # if the letter exists, we get its current count then increment
            letter[c] = letter.get(c,0) + 1
    return letter

def generate_report(letter):
    letter_list = []
    for char, count in letter.items():
        letter_list.append({"char": char, "count" : count})
    def sort_key(d):
        return d["count"]
    letter_list.sort(key= sort_key, reverse = True)
    return letter_list
    

