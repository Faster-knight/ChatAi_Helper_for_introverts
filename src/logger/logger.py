import logging
import os as __os

loger_module = logging.getLogger(__name__)
module_path = __os.path.dirname(__file__)


def setupLogger(envData: dict):
    if "MODE" not in list(envData.keys()):
        envData["MODE"] = "notdata"
    if not isinstance(envData["MODE"], str):
        envData["MODE"] = "notdata"
    temp = {
        "dev": logging.INFO,
        "prod": logging.WARNING,
        "notdata": logging.DEBUG
    }
    logging.basicConfig(filename="app-cental-log.log", level=temp[envData["MODE"].lower()])
    loger_module.log(level=logging.INFO, msg=f"Setup application logger on level: {temp[envData["MODE"].lower()]}")
