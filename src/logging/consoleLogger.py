from src.logging.logger import Logger


class Console_Logger(Logger):
    
    
    def __init__(self, min_log_level: tuple=None) -> None:
        super().__init__(min_log_level)
    
    
    def log(self, message: str=None, level: tuple=Logger.INFO) -> None:
        if not self.is_level_valid(level):
            raise ValueError(f"{Logger.ERROR[0]}Error: Log-level is not valid.")
        if message is None:
            raise ValueError(f"{Logger.ERROR[0]}Error: Log-message can not be empty.")
        print(f"{level[0]}{level[1]}: {message}{Logger.ENDL[0]}")