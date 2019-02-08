import unittest
import math
import lib.splicer_class


class TestSplicerMethods(unittest.TestCase):

    def test_construction(self):
        text = "Olafs gsgsn gsngs . gsgsgsgsgs. gsgsgsgs,"
        splicer = lib.splicer_class.Splicer(_text=text, _delimiting_size=5)
        self.assertEqual(len(splicer.get_split()), math.ceil(len(text)/5))
