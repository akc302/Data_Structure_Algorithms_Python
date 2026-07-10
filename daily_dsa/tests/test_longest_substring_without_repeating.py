import unittest

from daily_dsa.sliding_window.longest_substring_without_repeating import (
    length_of_longest_substring,
)


class TestLongestSubstringWithoutRepeating(unittest.TestCase):
    def test_finds_window_before_duplicate(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_handles_all_same_character(self):
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    def test_moves_left_past_previous_duplicate(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_handles_empty_string(self):
        self.assertEqual(length_of_longest_substring(""), 0)

    def test_treats_case_and_space_as_distinct_characters(self):
        self.assertEqual(length_of_longest_substring("Aa bB"), 5)


if __name__ == "__main__":
    unittest.main()
