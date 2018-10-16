import unittest

from lab_2.main import choose_best


class ChooseBestTest(unittest.TestCase):
    '''Tests choosing the best candidate to correct the spelling'''

    def test_choose_best_ideal(self):
        """ideal case for choosing the best candidate"""
        expected_word = 'lust'
        freq_dict = dict(list=1, lust=2)
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst')
        result = choose_best(freq_dict, candidates)
        self.assertEqual(expected_word, result)

    def test_choose_best_equal_freq(self):
        """Some words have the same freq - return sorted in alphabetical order"""
        expected_word = 'last'
        freq_dict = dict(list=1, lust=2, last=2)
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst', 'last')
        result = choose_best(freq_dict, candidates)
        self.assertEqual(expected_word, result)

    def test_choose_best_candidates_empty(self):
        """Candidates is empty"""
        expected_word = 'UNK'
        freq_dict = dict(list=1, lust=2)
        candidates = tuple([])
        result = choose_best(freq_dict, candidates)
        self.assertEqual(expected_word, result)

    def test_choose_best_candidates_none(self):
        """Candidates is none"""
        expected_word = 'UNK'
        freq_dict = dict(list=1, lust=2)
        result = choose_best(freq_dict, None)
        self.assertEqual(expected_word, result)

    def test_choose_best_candidates_has_not_str(self):
        """Candidates contains element that is not str"""
        expected_word = 'lust'
        freq_dict = dict(list=1, lust=2)
        candidates = ('lwst', 'lrst', 3, 'lust', 2)
        result = choose_best(freq_dict, candidates)
        self.assertEqual(expected_word, result)

    def test_choose_best_freq_dict_empty(self):
        """freq dict is empty"""
        expected_word = 'UNK'
        freq_dict = dict()
        candidates = ('lwst', 'lrst', 'lust')
        result = choose_best(freq_dict, candidates)
        self.assertEqual(expected_word, result)

    def test_choose_best_freq_dict_none(self):
        """freq dict is None"""
        expected_word = 'UNK'
        candidates = ('lwst', 'lrst', 'lust')
        result = choose_best(None, candidates)
        self.assertEqual(expected_word, result)

    def test_choose_best_freq_has_not_str(self):
        """freq dict has not str keys"""
        expected_word = 'list'
        freq_dict = {1: 5, 'list': 2}
        candidates = ('lwst', 'lrst', 'list')
        result = choose_best(freq_dict, candidates)
        self.assertEqual(expected_word, result)

    def test_choose_best_both_none(self):
        """Both params are None"""
        expected_word = 'UNK'
        result = choose_best(None, None)
        self.assertEqual(expected_word, result)
