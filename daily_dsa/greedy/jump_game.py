"""
Problem Statement:
Given a sequence of non-negative integers, where each value is the maximum
number of positions that can be jumped forward, determine whether the last
position can be reached from the first position.

Approach:
Scan from left to right while tracking the furthest reachable index. If the
current index is beyond that boundary, it cannot be reached. Otherwise extend
the boundary with the current jump length. Reaching or passing the last index
means the answer is true.

Time Complexity: O(n), where n is the number of positions.
Space Complexity: O(1), because only one reach boundary is stored.
"""

from collections.abc import Sequence


def can_reach_end(jumps: Sequence[int]) -> bool:
    """Return whether the final position is reachable from the first.

    Raises:
        ValueError: If any jump length is negative.
    """
    furthest_reachable = 0

    for index, jump_length in enumerate(jumps):
        if jump_length < 0:
            raise ValueError("jump lengths must be non-negative")
        if index > furthest_reachable:
            return False

        furthest_reachable = max(furthest_reachable, index + jump_length)
        if furthest_reachable >= len(jumps) - 1:
            return True

    return True
