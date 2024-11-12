import unittest

from scripts.analyze_data import filter_dirty_records


class TestDataUtils(unittest.TestCase):

    def test_filter_dirty_records(self):
        # Example data with some dirty records
        data = [
            {'flight_duration_secs': 3000, 'num_passengers': 150},
            {'flight_duration_secs': None, 'num_passengers': 200},
            {'flight_duration_secs': 3500, 'num_passengers': None}
        ]

        # Running the function
        clean_data, dirty_count = filter_dirty_records(data)

        # Assertions
        self.assertEqual(len(clean_data), 1)  # Only one valid record
        self.assertEqual(dirty_count, 2)  # Two dirty records


if __name__ == '__main__':
    unittest.main()
