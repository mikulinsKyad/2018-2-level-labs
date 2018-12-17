import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts):
        if texts is None or texts != list(texts):
        return []
    global_list = []
    new_text = []
    for huge_string in texts:
        if huge_string is None or type(huge_string) != str:
            continue
        end_string = huge_string + " "
        new_text.append(end_string)
    if not new_text:
        return []
    for huge_string in new_text:
        sentence_list = []
        word = ''
        may_be_break = "no"
        last_was_broken = "no"
        for symbol in huge_string:
            if symbol == " " or symbol == '\n':
                if symbol == " " and may_be_break == "yes" and word[-2:] == "br":
                    if last_was_broken == "yes":
                        word = ''
                        last_was_broken = "no"
                        continue
                    if word != '':
                        word = word.lower()
                        sentence_list.append(word[:-2])
                        word = ''
                        may_be_break = "no"
                        last_was_broken = "yes"
                elif word != '':
                    word = word.lower()
                    sentence_list.append(word)
                    word = ''
                continue
            if symbol == "<":
                may_be_break = "yes"
                continue
            if symbol in alpha_list:
                word += symbol
            if symbol not in alpha_list and symbol != ' ':
                continue
        global_list.append(sentence_list)
    return global_list


class TfIdfCalculator:
    
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []   # For each document.
        self.idf_values = {}  # For all documents
        self.tf_idf_values = []  # For each document
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
        
    def calculate_tf(self):
        for document in self.corpus:
            if document is None or type(document) != list:
                continue
            new_document = []
            for word in document:
                if type(word) != str:
                    continue
                else:
                    new_document.append(word)
            document_dict = {}
            sum_frequency = len(new_document)
            checked_words = list()
            for word in new_document:
                if type(word) != str:
                    continue
                if word not in checked_words:
                    checked_words.append(word)
                    term_frequency = new_document.count(word)
                    tf_idf = term_frequency/sum_frequency
                    document_dict[word] = tf_idf
            self.tf_values.append(document_dict)

    

    def calculate_idf(self):
        import math
        idf_dict = {}
        checked_words = list()
        new_corpus = []
        if self.corpus is None:
            return "ERROR"
        for document in self.corpus:
            if document is None:
                continue
            else:
                new_corpus.append(document)
        document_number = len(new_corpus)
        for document in new_corpus:
            document_checked_words = list()
            for word in document:
                if type(word) != str:
                    continue
                if word not in checked_words:
                    checked_words.append(word)
                    document_checked_words.append(word)
                    idf_dict[word] = 1
                elif word in checked_words and word not in document_checked_words:
                    document_checked_words.append(word)
                    idf_dict[word] += 1
        for key_word in idf_dict:
            idf_dict[key_word] = math.log(document_number/idf_dict[key_word])
        self.idf_values = idf_dict

    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return "ERROR"
        for small_dict in self.tf_values:
            tf_idf_dict = {}
            for word in small_dict:
                tf_idf_dict[word] = small_dict[word] * self.idf_values[word]
            self.tf_idf_values.append(tf_idf_dict)

    def report_on(self, word, document_index):
        if self.tf_idf_values is None or type(document_index) != int or document_index > (len(self.tf_idf_values) - 1) \
                or document_index < 0:
            return ()
        our_document_dict = self.tf_idf_values[document_index]
        if word not in our_document_dict:
            return ()
        else:
            tf_idf = our_document_dict[word]
        freq_list = []
        for one_word in sorted(our_document_dict, key=our_document_dict.get, reverse=True):
            freq_list.append(one_word)
        print(freq_list)
        place_dict = {}
        index = -1
        previous_word = ''
        for word_one in freq_list:
            if previous_word == '':
                place_dict[word_one] = 0
                index = 0
                previous_word = word_one
                continue
            if our_document_dict[word_one] == our_document_dict[previous_word]:
                place_dict[word_one] = index
                previous_word = word_one
                continue
            index += 1
            place_dict[word_one] = index
            previous_word = word_one
        print(place_dict)
        print(word)
        to_return = (tf_idf, place_dict[word])
        print(to_return)
        return to_return

    def dump_report_csv(self):
        file_data = open("report.csv", "w")
        if self.tf_values and self.idf_values and self.tf_idf_values:   # Creating the title
            file_data.write("word,")
            for file_name in self.file_names:
                name = "tf_" + file_name
                file_data.write(name + ";")  # В качестве разделителя -  ТОЧКА С ЗАПЯТОЙ
            file_data.write("idf,")          # Эксель так лучше воспринимает информацию
            string_to_write = ''
            for file_name in self.file_names:
                name = "tf_idf_" + file_name
                string_to_write += name + ";"
            string_to_write = string_to_write[:-1]
            file_data.write(string_to_write)
        for small_dict in self.tf_values:
            for word in small_dict:
                file_data.write('\n')
                string_for_word = word + ";"
                for dictionary in self.tf_values:
                    if word in dictionary:
                        string_for_word += str(dictionary[word]) + ";"
                    elif word not in dictionary:
                        string_for_word += str(0) + ","
                string_for_word += str(self.idf_values[word]) + ";"
                for dictionary in self.tf_idf_values:
                    if word in dictionary:
                        string_for_word += str(dictionary[word]) + ";"
                    elif word not in dictionary:
                        string_for_word += str(0) + ";"
                file_data.write(string_for_word[:-1])
        file_data.close()


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
