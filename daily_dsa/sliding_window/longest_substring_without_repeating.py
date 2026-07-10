"""
Problem: Longest Substring Without Repeating Characters

Given a string, return the length of the longest contiguous substring that
contains no repeated characters.

Approach:
Use a sliding window with a hash map from character to its most recent index.
Move the right edge across the string one character at a time. When a character
was already seen inside the current window, move the left edge just after that
previous occurrence. Track the largest valid window length seen during the scan.

Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(k), where k is the number of distinct characters in the
input string.
"""

from __future__ import annotations


def length_of_longest_substring(text: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0

    for right, char in enumerate(text):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
