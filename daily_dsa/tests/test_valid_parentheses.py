import unittest

from daily_dsa.stack.valid_parentheses import is_valid_parentheses


class TestValidParentheses(unittest.TestCase):
    def test_accepts_simple_balanced_pairs(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_accepts_nested_pairs(self):
        self.assertTrue(is_valid_parentheses("{[()]}"))

    def test_rejects_wrong_order(self):
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_rejects_unclosed_opening_bracket(self):
        self.assertFalse(is_valid_parentheses("(()"))

    def test_rejects_closing_bracket_without_opener(self):
        self.assertFalse(is_valid_parentheses("]"))

    def test_accepts_empty_string(self):
        self.assertTrue(is_valid_parentheses(""))


if __name__ == "__main__":
    unittest.main()
