"""
Problem: Valid Palindrome

Given a string, determine whether it is a palindrome after ignoring
non-alphanumeric characters and treating uppercase and lowercase letters as the
same.

Approach:
Use two pointers starting at the left and right ends of the string. Move each
pointer inward until it reaches an alphanumeric character, then compare those
characters case-insensitively. If every matched pair is equal, the normalized
string is a palindrome.

Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(1), because the scan compares characters in place.
"""

from __future__ import annotations


def is_valid_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1

        if text[left].casefold() != text[right].casefold():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_valid_palindrome("A man, a plan, a canal: Panama"))
