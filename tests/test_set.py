import unittest
from src.set import Set

class TestSet(unittest.TestCase):
    def test_set_empty(self):
        set = Set([])
        self.assertIsNone(set.average())
