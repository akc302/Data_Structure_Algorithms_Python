"""
Problem Statement:
Given a staircase with n steps, return the number of distinct ways to reach
the top when each move can climb either one or two steps.

Approach:
The ways to reach a step equal the sum of the ways to reach the previous one
and two steps before it. Keep only those two prior results and update them
iteratively until reaching n.

Time Complexity: O(n), where n is the number of steps.
Space Complexity: O(1), because only two running totals are stored.
"""


def count_climbing_ways(steps: int) -> int:
    """Return the number of one- and two-step sequences that climb *steps*.

    Raises:
        ValueError: If *steps* is negative.
    """
    if steps < 0:
        raise ValueError("steps must be non-negative")

    previous, current = 1, 1
    for _ in range(2, steps + 1):
        previous, current = current, previous + current

    return current
