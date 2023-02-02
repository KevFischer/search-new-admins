import os, sys, datetime, time

admin_values = [
    "Administrators",
    "Administratoren",
    "Administradores",
    "Administrateurs",
    "Administratorer",
    "Administratörer",
    "Administratorzy",
    "Пользователи",
]

starttime = datetime.datetime.now()
path = "C:/Users/wm01114/Desktop/reports/"
files = [path + file for file in os.listdir(path)]
files.sort(key=os.path.getmtime, reverse=True)

try:
    files = files[0:2]
except IndexError:
    raise Exception("\033[91m Error: There must be at least 2 files present.\033[0m")

all_data = []
for file in files:
    data = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            data.append(line.replace("\n", "").replace("\r", ""))
    all_data.append(data)

if all_data[0][0] != all_data[1][0]:
    raise Exception("\033[91m Error: CSV-Headers do not match.\033[0m")
keys = all_data[0][0].replace("\n", "").replace("\r", "").replace("\ufeff", "")
keys = keys.split(",")

if len(all_data[0][1].split(",")) != len(keys):
    raise Exception("\033[91m Error: Header length does not match with data set length.\033[0m")

diff = []
for set in all_data[0]:
    if set not in all_data[1]:
        if set.split(",")[2][0] == "w" and "_adm" not in set.split(",")[2]:
            if set.split(",")[1] in admin_values:
                diff.append(set)

formated_diff = []
for set in diff:
    json = {}
    for i in range(len(set.split(","))):
        json[keys[i]] = set.split(",")[i]
    formated_diff.append(json)

finished_in = datetime.timedelta.total_seconds(datetime.datetime.now() - starttime)

print(formated_diff)
print(len(formated_diff))
print(f"\033[92mFinished program in {finished_in} seconds.\033[0m")