import logging
import time

from application.utils.LoggingUtils import LoggingUtils
from application.services.first_circuit import create_first_circuit
from application.services import health_check
from qiskit import IBMQ


class Runner():

    def __init__(self, log_level=logging.INFO, console_log_level=None, application="Runner"):
        self.log_level = log_level
        self.console_log_level = console_log_level
        self.application = application

        try:
            self.logging_utils = self._init_logging()
            self.logging_utils.logApplicationStart()
        except Exception as err:
            print(f"Unable to instantiate logging.\n{err}")

    def _init_logging(self):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        loggingFile = f'logs/{self.application}-{timestamp}.log'
        loggingUtils = LoggingUtils(self.application, logFile=loggingFile,
                                    fileLevel=self.log_level, consoleLevel=self.console_log_level)
        
        return loggingUtils
    

    def _get_first_circuit(self):
        logging.getLogger()

        logging.info("Running function: create_first_circuit.")
        circuit = create_first_circuit()
        logging.info(f"Here is the return circuit:\n{circuit}")

    def run(self):
        try:
            logger = logging.getLogger()
            logging.info("Starting...")
            logging.info("Running...")
            print("Running...")

            # self._get_first_circuit()
            provider = IBMQ.get_provider("ibm-q")
            health_check.check_queues(provider, logger=logger)
        except Exception as err:
            logger.exception(err)
        finally:
            self.logging_utils.logApplicationFinish()
            logging.shutdown()
            print("Shutdown")
