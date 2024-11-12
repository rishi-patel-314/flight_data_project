from numpy import random

from utils.file_utils import ensure_directory_exists, write_json_to_file
from utils.data_utils import generate_random_flight
from constants.config import NUM_FILES, CITIES, FLIGHT_DATA_DIR
from datetime import datetime

def main():
    ensure_directory_exists(FLIGHT_DATA_DIR)
    total_records = 0

    for i in range(NUM_FILES):
        num_records = random.randint(50, 100)
        origin_city = random.choice(CITIES)
        date_prefix = datetime.now().strftime("%m-%y")
        filename = f"{FLIGHT_DATA_DIR}/{date_prefix}-{origin_city}-flights.json"

        flights_data = [generate_random_flight() for _ in range(num_records)]
        write_json_to_file(filename, flights_data)
        total_records += num_records

    print(f"Generated {total_records} flight records across {NUM_FILES} files.")

if __name__ == "__main__":
    main()
