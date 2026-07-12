"""
Problem: Valid Parentheses

Given a string containing only parentheses characters, determine whether every
opening bracket is closed by the same type of bracket and in the correct order.

Approach:
Scan the string from left to right while storing expected closing brackets on a
stack. For each opening bracket, push its matching closer. For each closing
bracket, it must match the most recent expected closer on top of the stack.
After the scan, the string is valid only when no unmatched open brackets remain.

Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(n), in the worst case when every character is an opening
bracket.
"""

from __future__ import annotations


def is_valid_parentheses(text: str) -> bool:
    expected_closers: list[str] = []
    matching_closers = {"(": ")", "[": "]", "{": "}"}

    for char in text:
        if char in matching_closers:
            expected_closers.append(matching_closers[char])
        elif not expected_closers or expected_closers.pop() != char:
            return False

    return not expected_closers


if __name__ == "__main__":
    print(is_valid_parentheses("()[]{}"))
