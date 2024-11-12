# utils/data_utils.py

import random
from datetime import datetime, timedelta

from constants.config import CITIES, MIN_FLIGHT_DURATION, MAX_FLIGHT_DURATION, MIN_PASSENGERS, MAX_PASSENGERS, \
    NULL_PROBABILITY


def generate_random_date():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))


def generate_random_flight():
    origin = random.choice(CITIES)
    destination = random.choice([city for city in CITIES if city != origin])
    flight_duration_secs = random.randint(MIN_FLIGHT_DURATION, MAX_FLIGHT_DURATION)
    num_passengers = random.randint(MIN_PASSENGERS, MAX_PASSENGERS)

    record = {
        "date": generate_random_date().strftime("%Y-%m-%d"),
        "origin_city": origin,
        "destination_city": destination,
        "flight_duration_secs": flight_duration_secs,
        "num_passengers": num_passengers,
    }

    if random.random() < NULL_PROBABILITY:
        key_to_nullify = random.choice(list(record.keys()))
        record[key_to_nullify] = None

    return record
