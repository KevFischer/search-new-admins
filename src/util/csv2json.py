from src.logging.logger import Logger


class CSV2JSON:
    
    
    def convert(self, keys: list=None, values: list=None) -> dict:
        if keys is None:
            raise Exception(f"{Logger.ERROR[0]}Error: Keys object can not be None.{Logger.ENDL[0]}")
        if values is None:
            raise Exception(f"{Logger.ERROR[0]}Error: Values object can not be None.{Logger.ENDL[0]}")
        if len(keys) != len(values):
            raise Exception(f"{Logger.ERROR[0]}Error: Amount of keys and values does not match.{Logger.ENDL[0]}")
        json = {}
        for i in range(len(keys)):
            json[keys[i]] = values[i]
        return json