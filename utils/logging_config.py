import logging
import os


def setup_logger(name, log_file=None, level=logging.INFO):
    """Function to configure and return a logger with both file and stream handlers."""

    # Create log directory in the root of the project
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # If log_file is provided, ensure it is within the log directory
    if log_file:
        log_file_path = os.path.join(log_dir, log_file)
    else:
        log_file_path = os.path.join(log_dir, 'flight_data_project.log')

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stream handler (for console output)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


# Initialize the logger for the project
project_logger = setup_logger('flight_data_project', 'flight_data_project.log')
