import unittest

import pandas as pd

from scripts.analyze_data import analyze_top_destinations, find_max_passenger_cities


class TestDataAnalysis(unittest.TestCase):

    def test_analyze_top_destinations(self):
        # Mock dataframe
        data = {
            'destination_city': ['NYC', 'LA', 'NYC', 'LA', 'SF'],
            'flight_duration_secs': [3000, 4000, 3500, 4500, 2000]
        }
        df = pd.DataFrame(data)

        # Running the analysis
        avg_duration, p95_duration = analyze_top_destinations(df)

        # Assertions
        self.assertEqual(avg_duration['NYC'], 3250)
        self.assertEqual(p95_duration['LA'], 4500)

    def test_find_max_passenger_cities(self):
        # Mock dataframe
        data = {
            'origin_city': ['NYC', 'LA', 'SF', 'LA'],
            'destination_city': ['LA', 'SF', 'NYC', 'NYC'],
            'num_passengers': [150, 200, 100, 50]
        }
        df = pd.DataFrame(data)

        # Running the analysis
        max_arrived_city, max_left_city = find_max_passenger_cities(df)

        # Assertions
        self.assertEqual(max_arrived_city, 'LA')
        self.assertEqual(max_left_city, 'NYC')


if __name__ == '__main__':
    unittest.main()
