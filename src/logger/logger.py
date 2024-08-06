import logging
import os as __os

loger_module = logging.getLogger(__name__)
module_path = __os.path.dirname(__file__)


def setupLogger(envData: dict):
    if "MODE" not in list(envData.keys()):
        logging.basicConfig(filename="app-central-log.log", level=logging.DEBUG)
