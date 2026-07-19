"""
Problem Statement:
Given the root of a binary tree, return its maximum depth. The maximum depth
is the number of nodes along the longest path from the root to a leaf.

Approach:
Use depth-first search recursively. An empty subtree has depth zero; otherwise,
the current subtree has depth one plus the greater depth of its left and right
subtrees.

Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the tree height, for the recursion stack.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    value: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))
