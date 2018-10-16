import unittest

from lab_2.main import keep_known


class KeepKnownTest(unittest.TestCase):
    """
    Tests deleting unknown words from candidates
    """

    def test_keep_known_ideal(self):
        """ Ideal case """
        freq_dict = dict(list=1, lust=2)
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst')
        expected = ['list', 'lust']
        known = keep_known(candidates, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidate_empty(self):
        """candidates is empty"""
        freq_dict = dict(list=1, lust=2)
        candidates = ()
        expected = []
        known = keep_known(candidates, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidate_none(self):
        """candidates is None"""
        freq_dict = dict(list=1, lust=2)
        candidates = None
        expected = []
        known = keep_known(candidates, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidate_not_str(self):
        """candidate contains el that is not str"""
        freq_dict = dict(list=1, lust=2)
        candidates = (1, 'list', 'lust', 'lwst')
        expected = ['list', 'lust']
        known = keep_known(candidates, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_not_tuple(self):
        """candidates type is not tuple"""
        freq_dict = dict(list=1, lust=2)
        candidates = ['list', 'lust', 'lwst']  # should be tuple
        expected = []
        known = keep_known(candidates, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_is_empty(self):
        """freq dict is empty"""
        freq_dict = dict()
        candidates = ('list', 'lust', 'lwst')
        expected = []
        known = keep_known(candidates, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_is_none(self):
        """freq dict is none"""
        candidates = ('list', 'lust', 'lwst')
        expected = []
        known = keep_known(candidates, None)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_has_not_str(self):
        """freq dict contains key that is not str"""
        freq_dict = {1: 5, 'list': 2}
        candidates = ('list', 'lust')
        expected = ['list']
        known = keep_known(candidates, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_all_none(self):
        """All params are None"""
        expected = []
        known = keep_known(None, None)
        self.assertCountEqual(expected, known)
