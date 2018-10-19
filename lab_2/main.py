"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

def propose_candidates(word, max_depth_permutations=1):
    alf_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
    num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if word == "" or word is None or max_depth_permutations not in num_lst:
        return []
    list_modifications_1 = []
    list_modifications_2 = []
    list_modifications_3 = []
    list_modifications_4 = []
    list_modifications = []

    for let_num in range(1, len(word) + 1):
        if let_num != -1:
            modified = word[:let_num - 1] + word[let_num:]
            list_modifications_1.append(modified)
        else:
            modified = word[:-1]
            list_modifications_1.append(modified)

    for let_num in range(len(word) + 1):
        if not let_num:
            for element in alf_lst:
                modified = element + word
                list_modifications_2.append(modified)
        elif let_num != -1:
            for element in alf_lst:
                modified = word[:let_num] + element + word[let_num:]
                list_modifications_2.append(modified)
        else:
            for element in alf_lst:
                modified = word + element
                list_modifications_2.append(modified)

    for let_num in range(1, len(word) + 1):
        if let_num != -1:
            for element in alf_lst:
                modified = word[:let_num - 1] + element + word[let_num:]
                list_modifications_3.append(modified)
        else:
            for element in alf_lst:
                modified = word[:-1] + element
                list_modifications_3.append(modified)

    for let_num in range(1, len(word)):
        if let_num != -1:
            modified = word[:let_num - 1] + word[let_num] + word[let_num - 1] + word[let_num + 1:]
            list_modifications_4.append(modified)

    list_modifications += list_modifications_1[:]
    list_modifications += list_modifications_2[:]
    list_modifications += list_modifications_3[:]
    list_modifications += list_modifications_4[:]
    list_modification = set(list_modifications)

    return list_modification


def keep_known(candidates, frequencies):
    if type(candidates) != tuple or candidates is None or frequencies == {} or frequencies is None:
        return []
    list_candidates = list(candidates)
    for candidate in candidates:
        if candidate not in frequencies:
            list_candidates.remove(candidate)
    all_candidates = list_candidates[:]
    return all_candidates


def choose_best(frequencies, candidates):
    if candidates == () or candidates is None or frequencies == {} or frequencies is None:
        return "UNK"
    best_candidates = []
    dict_candidates = []
    best = ""
    last_candidate = ""
    dict_func = frequencies.copy()
    if len(candidates) == 1:
        return candidates[0]
    for candidate in candidates:
        if candidate in dict_func:
            dict_candidates.append(candidate)
    for candidate in dict_candidates:
        if candidate == dict_candidates[0]:
            best = candidate
            last_candidate = candidate
            continue
        if dict_func[candidate] > dict_func[last_candidate]:
            best_candidates = []
            best = candidate
            last_candidate = candidate
        elif dict_func[candidate] == dict_func[last_candidate]:
            best_candidates.append(candidate)
            best_candidates.append(last_candidate)
            best_candy = sorted(best_candidates)
            best = best_candy[0]
            last_candidate = candidate
        else:
            best = last_candidate
    return best


def spell_check_word(frequencies, as_is_words, word):
    if as_is_words is None:
        as_is_words = ((),)
    if frequencies is None or word is None:
        return "UNK"
    if word.lower() in as_is_words or word.upper() in as_is_words:
        return word
    if word in frequencies:
        return word
    modified_candidates = propose_candidates(word)
    modified_candidates = tuple(modified_candidates)
    cleaned_candidates = keep_known(modified_candidates, frequencies)
    cleaned_candidates = tuple(cleaned_candidates)
    spell_checked_word = choose_best(frequencies, cleaned_candidates)
    return spell_checked_word
