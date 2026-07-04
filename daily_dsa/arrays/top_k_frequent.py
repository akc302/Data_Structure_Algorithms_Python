"""
Problem: Top K Frequent Elements

Given a list of integers and an integer k, return the k values that appear most
often. The answer may be returned in any order.

Approach:
Count each number with a hash map, then place numbers into frequency buckets.
Scanning buckets from highest frequency to lowest collects the most frequent
values without sorting every distinct number.

Time Complexity: O(n), where n is the number of input values.
Space Complexity: O(n), for the frequency map and buckets.
"""

from __future__ import annotations


def top_k_frequent(numbers: list[int], k: int) -> list[int]:
    if k <= 0:
        return []

    counts: dict[int, int] = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    if k > len(counts):
        raise ValueError("k cannot be greater than the number of distinct values.")

    buckets: list[list[int]] = [[] for _ in range(len(numbers) + 1)]
    for number, frequency in counts.items():
        buckets[frequency].append(number)

    result: list[int] = []
    for frequency in range(len(buckets) - 1, 0, -1):
        for number in buckets[frequency]:
            result.append(number)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
