import configparser

searchConfig = configparser.ConfigParser()
searchConfig.read("cfg/search.cfg")

admin_names = searchConfig["DEFAULT"]["admin_names"].replace("\n", "").split(",")


class AdminSearch:
    
    
    def search(self, data: list=None) -> list:
        if len(data) != 2:
            raise Exception(f"{Logger.ERROR[0]}Error: Can only compare 2 lists.{Logger.ENDL[0]}")
        if not isinstance(data[0], list):
            raise Exception(f"{Logger.ERROR[0]}Error: You need to compare lists.{Logger.ENDL[0]}")
        res = []
        for set in data[0]:
            if set not in data[1] and set.split(",")[2][0] == "w" and "_adm" not in set.split(",")[2] and set.split(",")[1] in admin_names:
                res.append(set)
        return res
    