import time
from functools import wraps
from utils.logging_config import project_logger  # assuming you have a logger configured

def measure_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # measure execution time for method
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        func_name = func.__name__
        msg = f"measure_it: func: {func_name}, time: {execution_time:.4f} seconds"
        project_logger.info(msg)
        return result

    return wrapper

def log_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # measure execution time for method
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        func_name = func.__name__
        msg = f"log_it: func: {func_name}, time: {execution_time:.4f} seconds"
        project_logger.info(msg)
        return result

    return wrapper
