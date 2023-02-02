class Logger:
    
    # Format: (Color, String, Value)
    INFO: str = ("\033[0m", "INFO", 0)
    NEW: str = ("\033[92m", "[+]", 1)
    WARN: str = ("\033[93m", "WARNING", 2)
    ERROR: str = ("\033[91m", "ERROR", 3)
    ENDL: str = ("\033[0m", "", 999)
    
    
    def __init__(self, min_log_level: tuple=None) -> None:
        self.min_log_level: tuple = min_log_level
    
    
    def is_level_valid(self, level: tuple=None) -> bool:
        if level is None:
            raise NameError(f"{Logger.ERROR}Error: Log-level can not be a NoneType object.")
        return level in [Logger.INFO, Logger.NEW, Logger.WARN, Logger.ERROR]
    
    
    def log(self, message: str=None, level: tuple=None) -> None:
        raise NotImplementedError(f"{Logger.ERROR[0]}Error: Can not call abstract method 'log()' from class Logger.")