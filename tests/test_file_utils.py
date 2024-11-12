import unittest
from unittest.mock import mock_open, patch

from utils.custom_exceptions import FileHandlingError
from utils.file_utils import read_json_from_file


class TestFileUtils(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"flight_duration_secs": 3000, "num_passengers": 150}]')
    def test_read_json_from_file_valid(self, mock_file):
        # Test reading valid JSON from a file
        data = read_json_from_file("test_data/valid_file.json")

        # Assertions
        self.assertEqual(len(data), 1)  # Should contain one record
        self.assertEqual(data[0]['flight_duration_secs'], 3000)

    @patch('builtins.open', new_callable=mock_open)
    def test_read_json_from_file_invalid(self, mock_file):
        # Test invalid JSON format or file read failure
        mock_file.side_effect = FileHandlingError("File reading error")

        with self.assertRaises(FileHandlingError):
            read_json_from_file("test_data/invalid_file.json")


if __name__ == '__main__':
    unittest.main()
