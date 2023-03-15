import unittest
from validate_papers import extract_paper


class TestExtractPaper(unittest.TestCase):

    def test1(self):
        dict1 = {'title': 'This is the title.\n',
                 'abstract': 'This is the abstract.\n',
                 'keywords': ['are', 'keywords', 'the', 'these'],
                 'introduction': 'This is the introduction.\n',
                 'body': 'This is the body.\n',
                 'conclusion': 'This is the conclusion.\n',
                 'references': ['SAliB, "A book," pp. 1–12, 2020.', 'Sajjad, "Another book," pp. 619–630, 2005.'],
                 'words_count': 35,
                 'pages_count': 1}
        dict2 = {'title': 'This is the title.\n',
                 'abstract': 'This is the abstract.\n',
                 'keywords': ['are', 'keywords', 'the', 'these'],
                 'introduction': 'This is the introduction.\n',
                 'body': 'This is the body.\n',
                 'conclusion': 'This is the conclusion.\n',
                 'references': ['SAliB, "A book," pp. 1–12, 2020.', 'Sajjad, "Another book," pp. 619–630, 2005.'],
                 'words_count': 35,
                 'pages_count': 2}
        self.assertDictEqual(extract_paper('paper2_sample.txt', 32), dict1)
        self.assertDictEqual(extract_paper('paper2_sample.txt', 300), dict2)

    def test_validations(self):
        with self.assertRaises(Exception) as t1:
            extract_paper('paper1_sample.txt', 16)

        exceptions = (
            str(t1.exception),
        )

        self.assertTupleEqual(exceptions, ("You can't put more than 5 keywords",))
