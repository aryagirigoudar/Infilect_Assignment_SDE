'''
Module used for logging
'''
from sys import stdout
from logging import getLogger, StreamHandler, FileHandler, INFO, Formatter

logger = getLogger()

formatter = Formatter(
    fmt='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

stream_handler = StreamHandler(stdout)
file_handler = FileHandler('app.log')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]
logger.setLevel(INFO)
