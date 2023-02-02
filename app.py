from src.logging.log import *
from src.logging.logger import Logger
from src.logging.fileLogger import File_Logger
from src.logging.consoleLogger import Console_Logger
from src.files.filereader import Filereader
from src.util.csv2json import CSV2JSON
from src.util.json2csv import JSON2CSV
from src.util.timer import Timer
from src.searchAdmins import AdminSearch
from datetime import datetime
import configparser, json


fileConfig = configparser.ConfigParser()
fileConfig.read("cfg/file.cfg")
input_dir = fileConfig["DEFAULT"]["report_dir"]
output_dir = fileConfig["DEFAULT"]["output_dir"]
output_type = fileConfig["DEFAULT"]["output_type"]

con_logger = Console_Logger()
f_logger = File_Logger(filename=datetime.now().strftime("%Y%m%d%H%M%S"))
register_logger(con_logger)
register_logger(f_logger)

filereader = Filereader()
converter = CSV2JSON()

def search_new() -> None:
    timer = Timer()
    timer.start()
    data = filereader.read_2_recent_files(input_dir)
    log(message=f"File reading done after {timer.stop()} seconds.", level=Logger.NEW)
    timer.start()
    new_admins = AdminSearch().search(data=data)
    log(message=f"Admin search done after {timer.stop()} seconds.", level=Logger.NEW)
    timer.start()
    formatted = [converter.convert(keys=data[0][0].split(","), values=admin.split(",")) for admin in new_admins]
    log(message=f"Converting to JSON format done after {timer.stop()} seconds.", level=Logger.NEW)
    log(message=f"Found {len(formatted)} new admins.", level=Logger.NEW)
    timer.start()
    if output_type in ["CSV", "ALL"]:
        conv = JSON2CSV()
        conv.convert(keys=formatted[0].keys(), data=formatted, outdir=output_dir)
        log(message=f"Generating CSV-File done.", level=Logger.NEW)
    if output_type in ["JSON", "ALL"]:
        output = json.dumps(formatted, indent=4)
        if not os.path.exists(os.path.join(os.getcwd(), output_dir)):
            os.mkdir(os.path.join(os.getcwd(), output_dir))
        with open(output_dir + datetime().now().strftime("%Y%m%d%H%M%S") + ".json", "a+", encoding="utf-8") as file:
            file.writelines(output)
        log(message=f"Generating JSON-File done.", level=Logger.NEW)
    log(message=f"Saving done after {timer.stop()} seconds.", level=Logger.NEW)
    
    
if __name__ == "__main__":
    search_new()
