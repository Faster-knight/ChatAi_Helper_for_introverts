"""
SPECIFICATION MODULE

Данный модуль выполняет роль загрузки параметров проекта при старте
Не рекомендуется писать в файле .env больше одного параметра в строке все сломается
"""
import os as __os


module_path = __os.path.dirname(__file__)
env_data = dict()


def ParseEnv(data: dict):
    temp = "/"
    with open(module_path + "/.env", "r", encoding="utf-8") as f:
        while temp != "":
            temp = f.readline()
            if temp == "":
                break
            sp = temp.split("=")
            sp[1] = sp[1].split("\n")[0]
            data[sp[0]] = sp[1]
    return data


def restartProdEnv(data: dict):
    return ParseEnv(data)
