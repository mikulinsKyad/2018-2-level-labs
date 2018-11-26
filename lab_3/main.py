"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}
        self.list_of_indexes = [0, 1, 2, 3, 4]

    def put(self, word):          
        if word is None or type(word) != str:
            return "ERROR"
        if word not in self.storage:
            word_index = self.list_of_indexes[0]
            self.storage[word] = word_index
            self.list_of_indexes.remove(self.list_of_indexes[0])
            self.list_of_indexes.append(self.list_of_indexes[-1] + 1)
            return word_index

    def get_id_of(self, word):
        if word is None or type(word) != str:
            return -1
        if word not in self.storage:
            return -1
        return self.storage[word]

    def get_original_by(self, id):
        for key, value in self.storage.items():
            if value == id:
                return key
        return "UNK"

    def from_corpus(self, corpus):
        if corpus is None or type(corpus) != tuple:
            return "ERROR"
        for word in corpus:
            self.put(word)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence):
        if type(sentence) != tuple:
            return "ERROR"
        sentence_list = list(sentence)      
        counter = self.size                                     
        gram = []
        for word_index in range(len(sentence_list)):    
            if len(sentence_list[word_index:counter + word_index]) < counter:
                break
            for coded_word in sentence_list[word_index:counter + word_index]:    
                gram.append(coded_word)
            gram = tuple(gram)
            if gram in self.gram_frequencies:
                self.gram_frequencies[gram] += 1
            else:
                self.gram_frequencies[gram] = 1
            gram = []
        return "OK"

    def calculate_log_probabilities(self):
        import math
        checking_dict = self.gram_frequencies.copy()
        for gram in self.gram_frequencies:
            sum_prefix_frequency = 0
            gram_frequency = self.gram_frequencies[gram]
            for gram1 in checking_dict:
                if gram1[0:-1] == gram[0:-1]:
                    sum_prefix_frequency += self.gram_frequencies[gram1]
            self.gram_log_probabilities[gram] = math.log(gram_frequency/sum_prefix_frequency)

    def predict_next_sentence(self, prefix):
        if type(prefix) != tuple or len(prefix) != self.size - 1:
            return []
        import random
        will_be_sentence = list(prefix)
        predictor = prefix
        predictor_counter = 0
        while True:
            gram_list = []
            for gram in self.gram_log_probabilities:
                if gram[0:-1] == predictor:
                    gram_list.append(gram)
            if not gram_list:
                break
            predictor_counter += 1
            possible_grams = {}
            possible_grams_equal_frequency = []
            for gram in self.gram_log_probabilities:
                if gram[0:-1] == predictor:
                    possible_grams[gram] = self.gram_log_probabilities[gram]
            next_element_frequency = possible_grams[max(possible_grams, key=lambda key: possible_grams[key])]
            for gram in self.gram_log_probabilities:
                if self.gram_log_probabilities[gram] == next_element_frequency:
                    possible_grams_equal_frequency.append(int(gram[self.size - 1]))
            next_element = random.choice(possible_grams_equal_frequency)
            will_be_sentence.append(next_element)
            predictor = tuple(will_be_sentence[predictor_counter:])
        return will_be_sentence

       
def encode(storage_instance, corpus):
    corpus_copy = corpus[:]
    for sentence_list in corpus_copy:
        for num, word in enumerate(sentence_list):
            sentence_list[num] = storage_instance.storage[word]
    return list(corpus_copy)


def split_by_sentence(text):
    if text != str(text):
        return []
    checker = text.split(" ")
    if len(checker) == 1:
        return []
    alpha_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    global_list = []
    sentence_list = []
    word = ''
    signal = 0
    text += ' '
    for symbol in text:    
        if signal == 1 and symbol == " ":
            signal = 2
            if word != '':
                word = word.lower()
                sentence_list.append(word)
                word = ''
            continue
        if signal == 2 and (symbol == " " or symbol == '\n'):
            continue
        if symbol.isupper() and signal == 2:
            if word != '':
                word = word.lower()
                sentence_list.append(word)
                word = ''
            if sentence_list:
                sentence_list.append("</s>")
                sentence_list.reverse()
                sentence_list.append("<s>") 
                sentence_list.reverse()
                global_list.append(sentence_list)
                sentence_list = []
            signal = 0
        if (symbol.islower() or symbol not in alpha_list) and signal != 0:
            signal = 0
        if symbol in alpha_list:
            word += symbol
        elif symbol == ' ' or symbol == '\n':
            if word != '':
                word = word.lower()
                sentence_list.append(word)
                word = ''
        elif symbol not in alpha_list and symbol != ' ' and symbol != '.' and symbol != '!' and symbol != '?':
            continue
        elif symbol == '.' or symbol != '!' or symbol != '?':
            signal = 1
    if sentence_list:
        sentence_list.append("</s>")
        sentence_list.reverse()
        sentence_list.append("<s>") 
        sentence_list.reverse()
        global_list.append(sentence_list)

    return global_list
