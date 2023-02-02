from src.logging.logger import Logger
from datetime import datetime
import csv, os


class JSON2CSV:
    
    
    def convert(self, keys: list=None, data: dict=None, outdir: str="out/") -> dict:
        if keys is None:
            raise Exception(f"{Logger.ERROR[0]}Error: Keys object can not be None.{Logger.ENDL[0]}")
        if data is None:
            raise Exception(f"{Logger.ERROR[0]}Error: Data object can not be None.{Logger.ENDL[0]}")
        if not os.path.exists(os.path.join(os.getcwd(), outdir)):
            os.mkdir(os.path.join(os.getcwd(), outdir))
        with open(outdir + datetime.now().strftime("%Y%m%d%H%M%S", ) + ".csv", "a+", encoding="utf-8", newline="") as file:
                dict_writer = csv.DictWriter(file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)