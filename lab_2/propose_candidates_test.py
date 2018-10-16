import unittest

from lab_2.main import propose_candidates


class ProposeCandidatesTest(unittest.TestCase):
    """
    Tests dictionary creation
    """

    def test_propose_candidates_ideal(self):
        """
           Ideal scenario. Good text.
        """
        test_word = 'cat'
        expected_modifications = [
            'at', 'ct', 'ca', 'act', 'cta', 'aat', 'bat', 'cat', 'dat', 'eat', 'fat', 'gat', 'hat', 'iat', 'jat', 'kat',
            'lat', 'mat', 'nat', 'oat', 'pat', 'qat', 'rat', 'sat', 'tat', 'uat', 'vat', 'wat', 'xat', 'yat', 'zat',
            'cbt', 'cct', 'cdt', 'cet', 'cft', 'cgt', 'cht', 'cit', 'cjt', 'ckt', 'clt', 'cmt', 'cnt', 'cot',
            'cpt', 'cqt', 'crt', 'cst', 'ctt', 'cut', 'cvt', 'cwt', 'cxt', 'cyt', 'czt', 'caa', 'cab', 'cac', 'cad',
            'cae', 'caf', 'cag', 'cah', 'cai', 'caj', 'cak', 'cal', 'cam', 'can', 'cao', 'cap', 'caq', 'car', 'cas',
            'cau', 'cav', 'caw', 'cax', 'cay', 'caz', 'acat', 'bcat', 'dcat', 'ecat', 'fcat', 'gcat',
            'hcat', 'icat', 'jcat', 'kcat', 'lcat', 'mcat', 'ncat', 'ocat', 'pcat', 'qcat', 'rcat', 'scat', 'tcat',
            'ucat', 'vcat', 'wcat', 'xcat', 'ycat', 'zcat', 'cbat', 'ccat', 'cdat', 'ceat', 'cfat', 'cgat',
            'chat', 'ciat', 'cjat', 'ckat', 'clat', 'cmat', 'cnat', 'coat', 'cpat', 'cqat', 'crat', 'csat', 'ctat',
            'cuat', 'cvat', 'cwat', 'cxat', 'cyat', 'czat', 'caat', 'cabt', 'cact', 'cadt', 'caet', 'caft', 'cagt',
            'caht', 'cait', 'cajt', 'cakt', 'calt', 'camt', 'cant', 'caot', 'capt', 'caqt', 'cart', 'cast', 'catt',
            'caut', 'cavt', 'cawt', 'caxt', 'cayt', 'cazt', 'cata', 'catb', 'catc', 'catd', 'cate', 'catf', 'catg',
            'cath', 'cati', 'catj', 'catk', 'catl', 'catm', 'catn', 'cato', 'catp', 'catq', 'catr', 'cats',
            'catu', 'catv', 'catw', 'catx', 'caty', 'catz'
        ]
        modifications = propose_candidates(test_word)
        self.assertCountEqual(expected_modifications, modifications)

    def test_propose_candidates_empty(self):
        test_word = ''
        expected = []
        modifications = propose_candidates(test_word)
        self.assertEqual(expected, modifications)

    def test_propose_candidates_none(self):
        expected = []
        modifications = propose_candidates(None)
        self.assertEqual(expected, modifications)

    def test_propose_candidates_duplicates(self):
        test_word = 'cat'
        counter = 0
        modifications = propose_candidates(test_word)
        self.assertEqual(len(modifications), len(set(modifications)))

    def test_propose_candidates_one_symbol(self):
        test_word = 'c'
        expected = ['', 'cn', 'cl', 'q', 'cr', 'sc', 'cv', 'w', 'p', 'u', 'oc', 'cx', 'g', 'y', 'cj', 'e', 'fc', 'd',
                    'v', 'vc', 'ce', 'ct', 'cd', 'gc', 'n', 't', 'ca', 'cf', 'b', 'cm', 'ci', 'xc', 'k', 'lc', 'h', 's',
                    'l', 'bc', 'i', 'qc', 'cb', 'c', 'a', 'x', 'nc', 'pc', 'cp', 'cu', 'kc', 'mc', 'cg', 'wc', 'ck',
                    'cz', 'r', 'ec', 'co', 'z', 'j', 'rc', 'm', 'cy', 'uc', 'ac', 'zc', 'ic', 'cw', 'yc', 'cs', 'o',
                    'jc', 'cc', 'ch', 'tc', 'hc', 'cq', 'dc', 'f']
        modifications = propose_candidates(test_word)
        self.assertCountEqual(expected, modifications)

    def test_propose_candidates_depth_permutations_not_num(self):
        expected = []
        modifications = propose_candidates('cat', '2')
        self.assertEqual(expected, modifications)

    def test_propose_candidates_depth_permutations_not_valid_number(self):
        expected = []
        modifications = propose_candidates('cat', -1)
        self.assertEqual(expected, modifications)

    def test_propose_candidates_depth_permutations_none(self):
        expected = []
        modifications = propose_candidates('cat', None)
        self.assertEqual(expected, modifications)

    # def test_propose_candidates_depth_permutations_ideal(self):
    #     expected_len = 14352
    #     modifications = propose_candidates('cat', 2)
    #     self.assertEqual(expected_len, len(modifications))
