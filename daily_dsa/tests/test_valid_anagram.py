import unittest

from daily_dsa.arrays.valid_anagram import is_anagram


class TestValidAnagram(unittest.TestCase):
    def test_returns_true_for_reordered_characters(self):
        self.assertTrue(is_anagram("listen", "silent"))

    def test_returns_false_for_different_lengths(self):
        self.assertFalse(is_anagram("rat", "carpet"))

    def test_returns_false_when_counts_differ(self):
        self.assertFalse(is_anagram("aacc", "ccac"))

    def test_handles_empty_strings(self):
        self.assertTrue(is_anagram("", ""))

    def test_treats_case_as_significant(self):
        self.assertFalse(is_anagram("DebitCard", "badcredit"))


if __name__ == "__main__":
    unittest.main()
