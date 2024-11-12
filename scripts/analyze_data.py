import os
import pandas as pd
from utils.file_utils import read_json_from_file
from constants.config import FLIGHT_DATA_DIR
from utils.logging_config import project_logger
from utils.custom_exceptions import FileHandlingError, DataProcessingError

def collect_flight_data(directory):
    """Collects flight data from JSON files in the specified directory."""
    dirty_records = 0
    all_flight_data = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                data = read_json_from_file(file_path)
                clean_data, dirty_count = filter_dirty_records(data)
                all_flight_data.extend(clean_data)
                dirty_records += dirty_count
                project_logger.info(f"Processed file: {file_path} with {dirty_count} dirty records.")
            except (FileHandlingError, IOError) as e:
                dirty_records += 1
                project_logger.error(f"Error reading file {file_path}: {e}")

    return all_flight_data, dirty_records

def filter_dirty_records(data):
    """Filters dirty records (containing None values) from the data."""
    clean_data = []
    dirty_count = 0

    for record in data:
        if None in record.values():
            dirty_count += 1
        else:
            clean_data.append(record)

    return clean_data, dirty_count

def process_flight_data(data):
    """Processes flight data using a DataFrame and performs analysis."""
    df = pd.DataFrame(data)
    df['flight_duration_secs'] = pd.to_numeric(df['flight_duration_secs'], errors='coerce')
    df['num_passengers'] = pd.to_numeric(df['num_passengers'], errors='coerce')
    df = df.dropna()

    return df

def analyze_top_destinations(df):
    """Analyzes top 25 destination cities based on flight duration."""
    top_dest_cities = df['destination_city'].value_counts().head(25).index
    top_dest_data = df[df['destination_city'].isin(top_dest_cities)]

    avg_duration = top_dest_data.groupby('destination_city')['flight_duration_secs'].mean()
    p95_duration = top_dest_data.groupby('destination_city')['flight_duration_secs'].quantile(0.95)

    return avg_duration, p95_duration

def find_max_passenger_cities(df):
    """Finds cities with the maximum passengers arrived and left."""
    passengers_arrived = df.groupby('destination_city')['num_passengers'].sum()
    passengers_left = df.groupby('origin_city')['num_passengers'].sum()

    max_arrived_city = passengers_arrived.idxmax()
    max_left_city = passengers_left.idxmax()

    return max_arrived_city, max_left_city

def main():
    project_logger.info("Data analysis started.")
    try:
        all_flight_data, dirty_records = collect_flight_data(FLIGHT_DATA_DIR)

        if not all_flight_data:
            raise DataProcessingError("No valid flight data available for analysis.")

        df = process_flight_data(all_flight_data)
        avg_duration, p95_duration = analyze_top_destinations(df)
        max_arrived_city, max_left_city = find_max_passenger_cities(df)

        # Display results
        print(f"Total records processed: {len(all_flight_data) + dirty_records}")
        print(f"Total dirty records: {dirty_records}")
        print(f"Average flight duration for top 25 destinations:\n{avg_duration}")
        print(f"95th percentile of flight duration for top 25 destinations:\n{p95_duration}")
        print(f"City with maximum passengers arrived: {max_arrived_city}")
        print(f"City with maximum passengers left: {max_left_city}")

        project_logger.info("Data analysis completed successfully.")

    except DataProcessingError as dpe:
        project_logger.error(f"Data processing error: {str(dpe)}")
    except Exception as e:
        project_logger.error(f"Unexpected error: {str(e)}")
    finally:
        project_logger.info("Data analysis process ended.")

if __name__ == "__main__":
    main()
