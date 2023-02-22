import unittest
from src.set import Set


class TestSet(unittest.TestCase):
    def test_set_empty(self):
        set = Set([])

        self.assertIsNone(set.average())

    def test_set_with_an_element(self):
        set = Set([5])

        self.assertEqual(set.average(), 5)

    def test_set_with_two_elements(self):
        set = Set([5, 7])

        self.assertEqual(set.average(), 6)

    def test_set_n_elements(self):
        set = Set([2, 4, 8, 9, 10, 15])

        self.assertEqual(set.average(), (2 + 4 + 8 + 9 + 10 +15)/6)
