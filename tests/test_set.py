import unittest
from src.set import Set

class TestSet(unittest.TestCase):
    def test_set_empty(self):
        set = Set([])
        
        self.assertIsNone(set.average())

    def test_set_with_an_element(self):
        set = Set([5])
        
        self.assertEqual(set.average(), 5)
