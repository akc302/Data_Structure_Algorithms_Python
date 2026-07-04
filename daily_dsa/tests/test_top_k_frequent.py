import unittest

from daily_dsa.arrays.top_k_frequent import top_k_frequent


class TestTopKFrequent(unittest.TestCase):
    def test_returns_most_frequent_values(self):
        self.assertCountEqual(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_handles_single_requested_value(self):
        self.assertEqual(top_k_frequent([4, 4, 5, 5, 5, 6], 1), [5])

    def test_handles_negative_numbers(self):
        self.assertCountEqual(top_k_frequent([-1, -1, -2, -3, -3, -3], 2), [-3, -1])

    def test_returns_empty_list_for_non_positive_k(self):
        self.assertEqual(top_k_frequent([1, 2, 3], 0), [])

    def test_raises_when_k_exceeds_distinct_values(self):
        with self.assertRaises(ValueError):
            top_k_frequent([7, 7, 8], 3)


if __name__ == "__main__":
    unittest.main()
