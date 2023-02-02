from src.logging.logger import Logger
import os


class File_Logger(Logger):
    
    
    def __init__(self, filename: str="log.log", logpath: str="log/", min_log_level: tuple=None) -> None:
        super().__init__(min_log_level)
        self.filename: str = filename
        self.logpath: str = logpath
    
    
    def log(self, message: str=None, level: tuple=Logger.INFO) -> None:
        if not self.is_level_valid(level):
            raise ValueError(f"{Logger.ERROR[0]}Error: Log-level is not valid.")
        if message is None:
            raise ValueError(f"{Logger.ERROR[0]}Error: Log-message can not be empty.")
        if not os.path.exists(os.path.join(os.getcwd(), self.logpath)):
            os.mkdir(os.path.join(os.getcwd(), self.logpath))
        with open(self.logpath + self.filename, "a+") as file:
            file.writelines(f"{level[1]}: {message}\n")