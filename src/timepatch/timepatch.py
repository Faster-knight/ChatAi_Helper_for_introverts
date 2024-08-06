import os as __os
import logging
import ui_module

module_path = __os.path.dirname(__file__)
logger_module = logging.getLogger(__name__)

# TODO точка входа в timepatch


def getQtApplication():
    return ui_module.qtApp


def setQtApplication(params: list[str]):
    ui_module.resetQtApplication(params)
