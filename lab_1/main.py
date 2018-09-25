"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    if text != str(text):
        return {}
    word = ""
    dictionary = {}
    s_list = []
    text = text.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    text += " "
    for letter in text:
        if letter in letters:
            word += letter
        elif letter == " ":
            if word != "":
                s_list.append(word)
            word = ""
        else:
            if word != "":
                s_list.append(word)
            word = ""
    for str_in_list in s_list:
        dictionary[str_in_list] = s_list.count(str_in_list)
    return dictionary

def filter_stop_words(frequencies, stop_words):
    if frequencies is None:
        return {}
    stop_frequencies = frequencies.copy()
    if stop_words is None:
        return stop_frequencies
    stop_lst = []
    for key2 in stop_frequencies:
        stop_lst.append(key2)
    for key3 in stop_lst:
        if key3 != str(key3):
            del stop_frequencies[key3]
    for woord in stop_words:
        if woord in stop_frequencies:
            del stop_frequencies[woord]
    return stop_frequencies


def get_top_n(frequencies, top_n):
    import operator
    dict_func1 = frequencies.copy()
    if dict_func1 == {} or top_n <= 0:
        return ()
    lst_dict = sorted(dict_func1.items(), key=operator.itemgetter(1), reverse=True)
    lst_keys = []
    for element in lst_dict:
        lst_keys.append(element[0])
    if top_n >= len(lst_keys):
        return tuple(lst_keys)
    return tuple(lst_keys[:top_n])
