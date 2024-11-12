import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Function to configure and return a logger"""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Initialize a logger for the project
project_logger = setup_logger('flight_data_project', 'flight_data_project.log')
