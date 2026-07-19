"""
Problem: Number of Recent Calls

Design a counter that records request times and returns how many requests
happened in the inclusive time window [t - 3000, t] after each new request.
Request times are received in strictly increasing order.

Approach:
Use a queue to store request timestamps that are still inside the active
3000-millisecond window. When a new timestamp arrives, append it to the back of
the queue, then remove timestamps from the front while they are too old. The
queue length is the number of recent requests.

Time Complexity: O(1) amortized per ping because each timestamp is added once
and removed once.
Space Complexity: O(w), where w is the number of requests inside the active
time window.
"""

from __future__ import annotations

from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self._requests: deque[int] = deque()

    def ping(self, timestamp: int) -> int:
        window_start = timestamp - 3000
        self._requests.append(timestamp)

        while self._requests and self._requests[0] < window_start:
            self._requests.popleft()

        return len(self._requests)


if __name__ == "__main__":
    counter = RecentCounter()
    print([counter.ping(time) for time in (1, 100, 3001, 3002)])
