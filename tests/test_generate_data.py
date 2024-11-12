import unittest
from unittest.mock import patch

from scripts.analyze_data import collect_flight_data


class TestDataGeneration(unittest.TestCase):

    @patch('your_module.read_json_from_file')
    @patch('os.walk')
    def test_collect_flight_data_valid(self, mock_walk, mock_read_json):
        # Mocking os.walk to simulate directory structure and files
        mock_walk.return_value = [('root', [], ['file1.json', 'file2.json'])]

        # Mocking the data returned by read_json_from_file
        mock_read_json.side_effect = [
            [{'flight_duration_secs': 3000, 'num_passengers': 150}],
            [{'flight_duration_secs': 4000, 'num_passengers': 200}]
        ]

        # Running the function
        data, dirty_records = collect_flight_data("test_data/valid_data")

        # Assertions
        self.assertEqual(len(data), 2)  # 2 valid records
        self.assertEqual(dirty_records, 0)  # No dirty records

    @patch('your_module.read_json_from_file')
    @patch('os.walk')
    def test_collect_flight_data_invalid(self, mock_walk, mock_read_json):
        # Simulating invalid data or failure to read files
        mock_walk.return_value = [('root', [], ['file1.json'])]
        mock_read_json.side_effect = Exception("File reading error")

        # Running the function
        data, dirty_records = collect_flight_data("test_data/invalid_data")

        # Assertions
        self.assertEqual(len(data), 0)  # No valid records
        self.assertEqual(dirty_records, 1)  # 1 dirty record due to the exception


if __name__ == '__main__':
    unittest.main()
