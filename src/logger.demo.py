from app.internals import logger

# Initialize the logger to use throughout this module.
# The benefit is that the format and configuration for logging is defined
# once centrally inside app.internals.
_logger = logger(__name__)

# Call the Logger methods directly using the _logger object, as documented on
# https://docs.python.org/2/library/logging.html#logging.Logger.debug
_logger.info('foo %s', 'bar')
