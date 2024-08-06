import logging
import datetime
import os as __os

loger_module = logging.getLogger(__name__)
module_path = __os.path.dirname(__file__)


def setupLogger(envData: dict):
    if (
            "MODE" not in list(envData.keys()) or
            "LOG" not in list(envData.keys()) or
            "LOG_PROJECT_PATH" not in list(envData.keys())
    ):
        envData["MODE"] = "notdata"
        envData["LOG"] = "logging"
        envData["LOG_PROJECT_PATH"] = "logs/app-central-log.log"
    if not isinstance(envData["MODE"], str):
        envData["MODE"] = "notdata"
    temp = {
        "dev": logging.INFO,
        "prod": logging.WARNING,
        "notdata": logging.DEBUG
    }
    if envData["LOG"] == "clear":
        clearLogs(envData["LOG_PROJECT_PATH"])
    logging.basicConfig(
        filename=envData["LOG_PROJECT_PATH"],
        level=temp[envData["MODE"].lower()]
    )
    loger_module.log(
        level=logging.INFO,
        msg=f"|{datetime.datetime.now()}| Setup application logger on level: {temp[envData["MODE"].lower()]}"
    )


def clearLogs(*args):
    for i in range(len(args)):
        with open(args[i], "w", encoding="utf-8") as f:
            f.writelines([])
