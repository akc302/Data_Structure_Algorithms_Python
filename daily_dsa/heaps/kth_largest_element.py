"""
Problem Statement:
Given an unsorted list of integers and an integer k, return the kth largest
element in the list. The kth largest is determined by sorted position, not by
the number of distinct values.

Approach:
Maintain a min-heap containing the k largest values seen so far. Add each
value to the heap; whenever it grows beyond k items, remove its smallest
value. After processing the list, the heap root is the kth largest value.

Time Complexity: O(n log k), where n is the number of values.
Space Complexity: O(k) for the heap.
"""

from __future__ import annotations

import heapq
from collections.abc import Sequence


def kth_largest(numbers: Sequence[int], k: int) -> int:
    """Return the kth largest value in *numbers*.

    Raises:
        ValueError: If k is not between 1 and the number of values.
    """
    if not 1 <= k <= len(numbers):
        raise ValueError("k must be between 1 and the number of values")

    smallest_of_largest: list[int] = []
    for number in numbers:
        heapq.heappush(smallest_of_largest, number)
        if len(smallest_of_largest) > k:
            heapq.heappop(smallest_of_largest)

    return smallest_of_largest[0]
