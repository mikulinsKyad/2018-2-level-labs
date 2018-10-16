# pylint: skip-file
"""
Checks the first lab. Part about the getting n popular words
"""

import unittest

from lab_1 import main


class GetTopNTest(unittest.TestCase):
    """
    Tests getting n popular words
    """

    def test_get_top_n_ideal(self):
        """
        Check that we get top n words ideal case
        """

        filtered_dict = {
            'quick': 4,
            'brown': 3,
            'fox': 2,
            'jumps': 1,
            'lazy': 1,
            'dog': 1
        }
        expected_result = ('quick', 'brown', 'fox')
        top_words = main.get_top_n(filtered_dict, 3)
        self.assertEqual(expected_result, top_words)


    def test_get_top_n_empty(self):
        """
        Check that result is empty on empty filtered dict
        """
        expected_result = ()
        filtered_dict = {}
        top_words = main.get_top_n(filtered_dict, 3)
        self.assertEqual(expected_result, top_words)

    def test_get_top_n_overflow(self):
        """
        Check that we get all words if n > len dict
        """
        expected_result = ('fox',)
        filtered_dict = {'fox': 1}
        top_words = main.get_top_n(filtered_dict, 3)
        self.assertEqual(expected_result, top_words)
        

    def test_get_top_n_equal_order(self):
        """
        Check that we get top n words ideal case
        """
        expected_result = ('dog', 'fox', 'cat')
        filtered_dict = {'fox': 1, 'dog': 1, 'cat': 1, }
        top_words = main.get_top_n(filtered_dict, 3)
        self.assertCountEqual(expected_result, top_words)

    def test_get_top_n_below_zero(self):
        """
        Check that we get top n words ideal case
        """
        expected_result = ()
        filtered_dict = {'fox': 1, 'dog': 1, 'cat': 1}
        top_words = main.get_top_n(filtered_dict, -1)
        self.assertEqual(expected_result, top_words)

    def test_get_top_n_zero(self):
        """
        Check that we get top n words ideal case
        """
        expected_result = ()
        filtered_dict = {'fox': 1, 'dog': 1, 'cat': 1}
        top_words = main.get_top_n(filtered_dict, 0)
        self.assertEqual(expected_result, top_words)
