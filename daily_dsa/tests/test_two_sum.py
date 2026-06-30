import unittest

from daily_dsa.arrays.two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_returns_indices_for_basic_case(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))

    def test_handles_duplicate_values(self):
        self.assertEqual(two_sum([3, 3], 6), (0, 1))

    def test_handles_negative_values(self):
        self.assertEqual(two_sum([-4, 8, 2, 10], 6), (0, 3))

    def test_raises_when_no_pair_exists(self):
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 100)


if __name__ == "__main__":
    unittest.main()
