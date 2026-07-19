"""
Problem Statement:
Reverse a singly linked list and return its new head.

Approach:
Walk through the list while tracking the previously visited node. For each
node, save its next node, redirect its next pointer to the previous node, and
advance both pointers. After the traversal, the previous pointer is the new
head.

Time Complexity: O(n), where n is the number of nodes in the list.
Space Complexity: O(1), because the links are reversed in place.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    value: int
    next: Optional["ListNode"] = None


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
