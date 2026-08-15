import unittest

from daily_dsa.dynamic_programming.climbing_stairs import count_climbing_ways


class TestClimbingStairs(unittest.TestCase):
    def test_zero_steps_has_one_empty_way(self):
        self.assertEqual(count_climbing_ways(0), 1)

    def test_small_staircases(self):
        self.assertEqual(count_climbing_ways(1), 1)
        self.assertEqual(count_climbing_ways(2), 2)
        self.assertEqual(count_climbing_ways(3), 3)

    def test_larger_staircase(self):
        self.assertEqual(count_climbing_ways(10), 89)

    def test_negative_steps_are_rejected(self):
        with self.assertRaises(ValueError):
            count_climbing_ways(-1)


if __name__ == "__main__":
    unittest.main()
