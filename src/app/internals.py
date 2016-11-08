import logging


# Configure logging
FORMAT = '|'.join([
        '%(asctime)-15s',
        '%(levelname)s',
        '%(name)s',
        '%(message)s',
        ])

logging.basicConfig(format=FORMAT, level=logging.INFO)


def logger(name):
    return logging.getLogger(name)
