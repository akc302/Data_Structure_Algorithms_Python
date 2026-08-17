import unittest

from daily_dsa.greedy.jump_game import can_reach_end


class TestJumpGame(unittest.TestCase):
    def test_reaches_final_position(self):
        self.assertTrue(can_reach_end([2, 3, 1, 1, 4]))

    def test_stops_at_unreachable_position(self):
        self.assertFalse(can_reach_end([3, 2, 1, 0, 4]))

    def test_single_and_empty_sequences_are_reachable(self):
        self.assertTrue(can_reach_end([0]))
        self.assertTrue(can_reach_end([]))

    def test_negative_jump_length_is_rejected(self):
        with self.assertRaises(ValueError):
            can_reach_end([1, -1, 1])


if __name__ == "__main__":
    unittest.main()
