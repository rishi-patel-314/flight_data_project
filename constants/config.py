# constants/config.py

NUM_FILES = 5000
CITIES = [f"City_{i}" for i in range(100, 200)]
FLIGHT_DATA_DIR = "/Users/rishikanaujia/PycharmProjects/flight_data_project/tmp/flights"
MIN_FLIGHT_DURATION = 30 * 60  # 30 minutes in seconds
MAX_FLIGHT_DURATION = 5 * 60 * 60  # 5 hours in seconds
MIN_PASSENGERS = 10
MAX_PASSENGERS = 300
NULL_PROBABILITY = 0.001  # Probability of introducing null values

#log_configs
MAX_LOG_SIZE= 25 * 1024 * 1024
BACKUP_COUNT= 5