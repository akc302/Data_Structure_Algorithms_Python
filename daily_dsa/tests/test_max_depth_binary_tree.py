import unittest

from daily_dsa.trees.max_depth_binary_tree import TreeNode, max_depth


class TestMaxDepthBinaryTree(unittest.TestCase):
    def test_balanced_tree(self):
        root = TreeNode(
            3,
            left=TreeNode(9),
            right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
        )

        self.assertEqual(max_depth(root), 3)

    def test_skewed_tree(self):
        root = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4))))

        self.assertEqual(max_depth(root), 4)

    def test_single_node(self):
        self.assertEqual(max_depth(TreeNode(42)), 1)

    def test_empty_tree(self):
        self.assertEqual(max_depth(None), 0)


if __name__ == "__main__":
    unittest.main()
