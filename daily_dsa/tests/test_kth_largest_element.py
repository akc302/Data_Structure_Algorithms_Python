import unittest

from daily_dsa.heaps.kth_largest_element import kth_largest


class TestKthLargestElement(unittest.TestCase):
    def test_unsorted_values(self):
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_duplicate_values_count_toward_rank(self):
        self.assertEqual(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_negative_values(self):
        self.assertEqual(kth_largest([-10, -3, -7, -1], 3), -7)

    def test_single_value(self):
        self.assertEqual(kth_largest([42], 1), 42)

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            kth_largest([1, 2, 3], 0)

        with self.assertRaises(ValueError):
            kth_largest([1, 2, 3], 4)


if __name__ == "__main__":
    unittest.main()
