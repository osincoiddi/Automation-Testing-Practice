
import logging
import os
from logging import basicConfig

class LogGen:
    @staticmethod
    def loggen():
        path=os.path.abspath(os.path.abspath(os.curdir)+"/logs/automation.log")
        logging.basicConfig(filename=path,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s',datefmt='%d-%b-%y %H:%M:%S:%P')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
