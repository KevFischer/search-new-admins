from src.logging.logger import Logger
import os


class Filereader:
    
    
    def read_2_recent_files(self, dir: str=None) -> list:
        if dir is None:
            raise ValueError(f"{Logger.ERROR[0]}Error: Directory to read can not be NoneType object.{Logger.ENDL[0]}")
        files = [dir + file for file in os.listdir(dir)]
        files.sort(key=os.path.getmtime, reverse=True)
        try:
            files = files[0:2]
        except IndexError:
            raise Exception(f"{Logger.ERROR[0]}Error: There must be at least 2 files present.{Logger.ENDL[0]}")
        all_data = []
        for file in files:
            data = []
            with open(file, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    data.append(line.replace("\n", "").replace("\r", ""))
            all_data.append(data)
        return all_data