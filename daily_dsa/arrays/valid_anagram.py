"""
Problem: Valid Anagram

Given two strings, determine whether the second string is an anagram of
the first. An anagram uses exactly the same characters with the same
frequencies, only rearranged.

Approach:
Count characters from the first string in a hash map, subtract counts while
scanning the second string, and fail early if a character is missing or used
too many times. Matching lengths are checked first because anagrams must have
the same number of characters.

Time Complexity: O(n)
Space Complexity: O(k), where k is the number of distinct characters.
"""

from __future__ import annotations


def is_anagram(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    counts: dict[str, int] = {}
    for char in first:
        counts[char] = counts.get(char, 0) + 1

    for char in second:
        if char not in counts:
            return False

        counts[char] -= 1
        if counts[char] == 0:
            del counts[char]

    return not counts


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))
