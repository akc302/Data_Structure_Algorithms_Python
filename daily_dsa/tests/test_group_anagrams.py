import unittest

from daily_dsa.arrays.group_anagrams import group_anagrams


def normalize(groups):
    return sorted(sorted(group) for group in groups)


class TestGroupAnagrams(unittest.TestCase):
    def test_groups_words_with_same_letters(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]

        self.assertEqual(
            normalize(group_anagrams(words)),
            [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]],
        )

    def test_handles_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_groups_empty_strings(self):
        self.assertEqual(normalize(group_anagrams(["", "", "a"])), [["", ""], ["a"]])

    def test_preserves_duplicate_words(self):
        self.assertEqual(normalize(group_anagrams(["abc", "bca", "abc"])), [["abc", "abc", "bca"]])

    def test_rejects_non_lowercase_letters(self):
        with self.assertRaises(ValueError):
            group_anagrams(["Tea"])


if __name__ == "__main__":
    unittest.main()
