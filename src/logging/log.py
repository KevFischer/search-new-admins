from src.logging.logger import Logger


loggers = []


def register_logger(logger: Logger=None) -> None:
    if logger is None:
        raise NameError(f"{Logger.ERROR[0]}Error: Logger can not be NoneType object.")
    loggers.append(logger)
    
    
def get_loggers() -> list:
    return loggers


def remove_logger(logger: Logger=None) -> None:
    if logger is None:
        raise NameError(f"{Logger.ERROR[0]}Error: Logger can not be NoneType object.")
    loggers.remove(logger)
    
    
def remove_logger(index: int=None) -> None:
    if index is None:
        raise NameError(f"{Logger.ERROR[0]}Error: Logger can not be NoneType object.")
    loggers.remove(index)
    
    
def log(message: str=None, level: tuple=Logger.INFO) -> None:
    if message is None:
        raise ValueError(f"{Logger.ERROR[0]}Error: Log-message can not be empty.")
    for logger in loggers:
        if not logger.is_level_valid(level):
            raise ValueError(f"{Logger.ERROR[0]}Error: Log-level is not valid.")
        if logger.min_log_level is None:
            logger.log(message=message, level=level)
        elif level[2] >= logger.min_log_level[2]:
            logger.log(message=message, level=level)
            