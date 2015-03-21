import unittest
from trie import TrieNode


class TrieTest(unittest.TestCase):

    def setUp(self):
        self.keys = [
            "hill",
            "ho",
        ]
        self.expected_string = """
-h
--i
---l
----l
--o"""
        self.trob = TrieNode()
        for key in self.keys[0:2]:
            self.trob.insert(key)

    def test_keycheck1(self):
        # "Should always count empty string as present
        for key in self.keys[0:2]:
            self.assertTrue(self.trob.has_key(key), key)
        self.assertTrue(self.trob.has_key(""), "empty key")

    def test_as_string(self):
        self.assertEqual(self.expected_string, self.trob.as_string())

if __name__ == "__main__":
    unittest.main()
