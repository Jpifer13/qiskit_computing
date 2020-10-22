import logging
import time

from application.utils.LoggingUtils import LoggingUtils
from application.services.first_circuit import create_first_circuit


class Runner():

    def __init__(self, log_level=logging.DEBUG, console_log_level=None):
        self.log_level = log_level
        self.console_log_level = console_log_level

        try:
            self.logging_utils = self._init_logging()
            self.logging_utils.logApplicationStart()
        except:
            print("Unable to instantiate logging.")

    def _init_logging(self):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        loggingFile = f'logs/{self.application}-{timestamp}.log'
        loggingUtils = LoggingUtils(self.application, logFile=loggingFile,
                                    fileLevel=self.log_level, consoleLevel=self.console_log_level)
        
        return loggingUtils
    
    def run(self):
        circuit = create_first_circuit()
