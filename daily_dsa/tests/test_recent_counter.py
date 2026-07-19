import unittest

from daily_dsa.queue.recent_counter import RecentCounter


class TestRecentCounter(unittest.TestCase):
    def test_counts_requests_inside_initial_window(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(100), 2)
        self.assertEqual(counter.ping(3001), 3)
        self.assertEqual(counter.ping(3002), 3)

    def test_keeps_boundary_timestamp_in_window(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(10), 1)
        self.assertEqual(counter.ping(3010), 2)

    def test_evicts_multiple_old_requests(self):
        counter = RecentCounter()

        for timestamp in (1, 2, 3, 4):
            counter.ping(timestamp)

        self.assertEqual(counter.ping(6005), 1)

    def test_instances_do_not_share_state(self):
        first = RecentCounter()
        second = RecentCounter()

        self.assertEqual(first.ping(1), 1)
        self.assertEqual(first.ping(2), 2)
        self.assertEqual(second.ping(100), 1)


if __name__ == "__main__":
    unittest.main()
