class FlightDataError(Exception):
    """Base class for other exceptions"""
    pass


class FileHandlingError(FlightDataError):
    """Raised when there is an error handling a file"""
    pass


class DataProcessingError(FlightDataError):
    """Raised when there is an error processing data"""
    pass
