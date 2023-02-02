from src.logging.log import log, register_logger
from src.logging.logger import Logger
from src.logging.fileLogger import File_Logger
from src.logging.consoleLogger import Console_Logger
import os

register_logger(File_Logger())
register_logger(Console_Logger())

log(message="This is a test log.", level=Logger.NEW)