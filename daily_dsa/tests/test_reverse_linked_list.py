import unittest

from daily_dsa.linked_lists.reverse_linked_list import (
    ListNode,
    reverse_linked_list,
)


def to_values(head):
    values = []
    current = head

    while current is not None:
        values.append(current.value)
        current = current.next

    return values


class TestReverseLinkedList(unittest.TestCase):
    def test_reverses_multiple_nodes(self):
        third = ListNode(3)
        second = ListNode(2, third)
        head = ListNode(1, second)

        reversed_head = reverse_linked_list(head)

        self.assertEqual(to_values(reversed_head), [3, 2, 1])
        self.assertIs(reversed_head, third)
        self.assertIs(third.next, second)
        self.assertIs(second.next, head)
        self.assertIsNone(head.next)

    def test_single_node_remains_head(self):
        head = ListNode(7)

        self.assertIs(reverse_linked_list(head), head)
        self.assertIsNone(head.next)

    def test_empty_list_returns_none(self):
        self.assertIsNone(reverse_linked_list(None))


if __name__ == "__main__":
    unittest.main()
