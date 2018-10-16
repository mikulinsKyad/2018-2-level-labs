import unittest
from unittest.mock import patch

from lab_2.main import spell_check_word


class SpellCheckWordsTest(unittest.TestCase):
    """Checks the whole workflow of all functions"""

    def test_spell_check_word_ideal(self):
        """ideal case all data is as expected """
        freq_dict = dict(list=1, lust=2)
        word = 'lwst'
        as_is_words = ('LYST',)
        expected = 'lust'
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertEqual(expected, res)

    def test_spell_check_word_as_is_words_none(self):
        freq_dict = dict(list=1, lust=2)
        word = 'lwst'
        as_is_words = None
        expected = 'lust'
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertEqual(expected, res)

    def test_spell_check_word_dict_none(self):
        freq_dict = None
        word = 'lwst'
        as_is_words = ((),)
        expected = 'UNK'
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertEqual(expected, res)

    def test_spell_check_word_none(self):
        freq_dict = dict(list=1, lust=2)
        word = None
        as_is_words = ((),)
        expected = 'UNK'
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertEqual(expected, res)

    def test_spell_check_word_known(self):
        freq_dict = dict(list=1, lust=2)
        word = 'list'
        as_is_words = ((),)
        expected = 'list'
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertEqual(expected, res)

    def test_spell_check_word_in_as_is(self):
        freq_dict = dict(list=1, lust=2)
        word = 'lwst'
        as_is_words = ('LWST',)
        expected = 'lwst'
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertEqual(expected, res)

    @patch('lab_2.main.propose_candidates')
    @patch('lab_2.main.keep_known')
    @patch('lab_2.main.choose_best')
    def test_spell_check_word_functions_called_for_incorrect_word(self, propose_candidates, keep_known, choose_best):
        '''Checks that all 3 functions were called for unknown word'''
        freq_dict = dict(list=1, lust=2)
        word = 'lwst'
        as_is_words = ((),)
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertTrue(propose_candidates.called)
        self.assertTrue(keep_known.called)
        self.assertTrue(choose_best.called)

    @patch('lab_2.main.propose_candidates')
    @patch('lab_2.main.keep_known')
    @patch('lab_2.main.choose_best')
    def test_spell_check_word_functions_not_called_as_is_word(self, propose_candidates, keep_known, choose_best):
        '''Checks that all 3 functions were not called for as is word'''
        freq_dict = dict(list=1, lust=2)
        word = 'lwst'
        as_is_words = ('LWST',)
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertFalse(propose_candidates.called)
        self.assertFalse(keep_known.called)
        self.assertFalse(choose_best.called)

    @patch('lab_2.main.propose_candidates')
    @patch('lab_2.main.keep_known')
    @patch('lab_2.main.choose_best')
    def test_spell_check_word_functions_not_called_for_correct_word(self, propose_candidates, keep_known, choose_best):
        '''Checks that all 3 functions were not called for as is word'''
        freq_dict = dict(list=1, lust=2)
        word = 'list'
        as_is_words = ('LWST',)
        res = spell_check_word(freq_dict, as_is_words, word)
        self.assertFalse(propose_candidates.called)
        self.assertFalse(keep_known.called)
        self.assertFalse(choose_best.called)
