"""
Problem: Two Sum

Given a list of integers and a target, return the indices of two numbers
that add up to the target.

Approach:
Use a hash map from value to index. For each number, check whether its
complement has already been seen.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}

    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return seen[complement], index
        seen[number] = index

    raise ValueError("No two numbers add up to the target.")


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
