from src.logging.log import *
from src.logging.logger import Logger
from src.logging.fileLogger import File_Logger
from src.logging.consoleLogger import Console_Logger
from src.files.filereader import Filereader
from src.util.csv2json import CSV2JSON
from src.util.timer import Timer
from src.searchAdmins import AdminSearch
from datetime import datetime
import configparser


fileConfig = configparser.ConfigParser()
fileConfig.read("cfg/file.cfg")
input_dir = fileConfig["DEFAULT"]["report_dir"]
output_dir = fileConfig["DEFAULT"]["output_dir"]

con_logger = Console_Logger()
f_logger = File_Logger(filename=datetime.now().strftime("%Y%m%d%H%M%S"))
register_logger(con_logger)
register_logger(f_logger)

filereader = Filereader()
converter = CSV2JSON()

def search_new() -> None:
    data = filereader.read_2_recent_files(input_dir)
    new_admins = AdminSearch().search(data=data)
    formatted = [converter.convert(keys=data[0][0], values=admin) for admin in new_admins]
    log(message=formatted, level=Logger.NEW)
    
    
if __name__ == "__main__":
    search_new()
