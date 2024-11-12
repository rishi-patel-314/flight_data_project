# scripts/analyze_data.py
import json
import os
import pandas as pd
from utils.file_utils import read_json_from_file
from constants.config import FLIGHT_DATA_DIR

def main():
    dirty_records = 0
    all_flight_data = []

    for root, dirs, files in os.walk(FLIGHT_DATA_DIR):
        for file in files:
            try:
                data = read_json_from_file(os.path.join(root, file))
                for record in data:
                    if None in record.values():
                        dirty_records += 1
                    else:
                        all_flight_data.append(record)
            except (json.JSONDecodeError, IOError):
                dirty_records += 1

    df = pd.DataFrame(all_flight_data)
    df['flight_duration_secs'] = pd.to_numeric(df['flight_duration_secs'], errors='coerce')
    df['num_passengers'] = pd.to_numeric(df['num_passengers'], errors='coerce')
    df = df.dropna()

    top_dest_cities = df['destination_city'].value_counts().head(25).index
    top_dest_data = df[df['destination_city'].isin(top_dest_cities)]

    avg_duration = top_dest_data.groupby('destination_city')['flight_duration_secs'].mean()
    p95_duration = top_dest_data.groupby('destination_city')['flight_duration_secs'].quantile(0.95)

    passengers_arrived = df.groupby('destination_city')['num_passengers'].sum()
    passengers_left = df.groupby('origin_city')['num_passengers'].sum()

    max_arrived_city = passengers_arrived.idxmax()
    max_left_city = passengers_left.idxmax()

    print(f"Total records processed: {len(all_flight_data) + dirty_records}")
    print(f"Total dirty records: {dirty_records}")
    print(f"Average flight duration for top 25 destinations:\n{avg_duration}")
    print(f"95th percentile of flight duration for top 25 destinations:\n{p95_duration}")
    print(f"City with maximum passengers arrived: {max_arrived_city}")
    print(f"City with maximum passengers left: {max_left_city}")

if __name__ == "__main__":
    main()
