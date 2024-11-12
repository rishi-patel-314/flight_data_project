import os
import random
from datetime import datetime

from constants.config import NUM_FILES, CITIES, FLIGHT_DATA_DIR
from utils.data_utils import generate_random_flight
from utils.file_utils import ensure_directory_exists, write_json_to_file
from utils.logger import measure_it, log_it
from utils.logging_config import project_logger


@measure_it
@log_it
def generate_flight_data_for_file(file_path, num_records):
    """Generates flight data and writes it to the specified file."""
    try:
        flights_data = [generate_random_flight() for _ in range(num_records)]
        write_json_to_file(file_path, flights_data)
        project_logger.info(f"Generated {num_records} flight records in {file_path}.")
        return num_records
    except Exception as e:
        project_logger.error(f"Error generating data for {file_path}: {e}")
        return 0


def generate_filename(origin_city):
    """Generates a filename for storing flight data."""
    date_prefix = datetime.now().strftime("%m-%y")
    return os.path.join(FLIGHT_DATA_DIR, f"{date_prefix}-{origin_city}-flights.json")


@measure_it
@log_it
def generate_flight_data():
    """Generates flight data across multiple files and returns the total record count."""
    ensure_directory_exists(FLIGHT_DATA_DIR)
    total_records = 0

    for i in range(NUM_FILES):
        num_records = random.randint(50, 100)
        origin_city = random.choice(CITIES)
        file_path = generate_filename(origin_city)

        records_generated = generate_flight_data_for_file(file_path, num_records)
        total_records += records_generated

    return total_records


def main():
    """Main function to generate flight data."""
    project_logger.info("Flight data generation started.")
    total_records = generate_flight_data()
    project_logger.info(f"Generated {total_records} flight records across {NUM_FILES} files.")
    print(f"Generated {total_records} flight records across {NUM_FILES} files.")


if __name__ == "__main__":
    main()
