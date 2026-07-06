"""
Problem: Group Anagrams

Given a list of strings, group words that are anagrams of each other. Words are
anagrams when they contain the same characters with the same frequencies.

Approach:
Build a hash map from each word's character-frequency signature to the words
that share it. A 26-slot tuple is used as the signature so words can be grouped
in linear time without sorting every word.

Time Complexity: O(n * m), where n is the number of words and m is the maximum
word length.
Space Complexity: O(n * m), for the grouped output and hash map keys.
"""

from __future__ import annotations


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = {}

    for word in words:
        counts = [0] * 26
        for character in word:
            if not "a" <= character <= "z":
                raise ValueError("group_anagrams expects lowercase English letters only.")
            counts[ord(character) - ord("a")] += 1

        signature = tuple(counts)
        groups.setdefault(signature, []).append(word)

    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
