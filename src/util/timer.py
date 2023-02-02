from datetime import datetime


class Timer:
    
    
    def __init__(self) -> None:
        self.starttime: datetime = None
        
    
    def start(self) -> None:
        if self.starttime is not None:
            raise Exception(f"{Logger.ERROR[0]}Error: Can not start same timer when already running.{Logger.ENDL[0]}")
        self.starttime = datetime.now()
        
        
    def stop(self) -> float:
        if self.starttime is None:
            raise Exception(f"{Logger.ERROR[0]}Error: Can not stop a not running timer.{Logger.ENDL[0]}")
        start = self.starttime
        self.starttime = None
        return datetime.timedelta.total_seconds(datetime.datetime.now() - start)
        