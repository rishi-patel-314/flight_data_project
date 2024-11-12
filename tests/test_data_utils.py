# tests/test_data_utils.py

import unittest
from utils.data_utils import generate_random_flight


class TestDataUtils(unittest.TestCase):
    def test_generate_random_flight(self):
        flight = generate_random_flight()
        self.assertIn("origin_city", flight)
        self.assertIn("destination_city", flight)
        self.assertGreaterEqual(flight["flight_duration_secs"], 30 * 60)
        self.assertLessEqual(flight["flight_duration_secs"], 5 * 60 * 60)


if __name__ == "__main__":
    unittest.main()
