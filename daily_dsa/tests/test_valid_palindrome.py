import unittest

from daily_dsa.two_pointers.valid_palindrome import is_valid_palindrome


class TestValidPalindrome(unittest.TestCase):
    def test_accepts_sentence_with_punctuation(self):
        self.assertTrue(is_valid_palindrome("A man, a plan, a canal: Panama"))

    def test_rejects_non_palindrome(self):
        self.assertFalse(is_valid_palindrome("race a car"))

    def test_accepts_empty_normalized_string(self):
        self.assertTrue(is_valid_palindrome("., "))

    def test_accepts_mixed_case_and_digits(self):
        self.assertTrue(is_valid_palindrome("12 No 'x' in Nixon 21"))

    def test_rejects_digit_mismatch(self):
        self.assertFalse(is_valid_palindrome("ab2a"))


if __name__ == "__main__":
    unittest.main()
