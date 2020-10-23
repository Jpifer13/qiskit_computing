import logging
import time

from application.utils.LoggingUtils import LoggingUtils
from application.services.circuits import create_first_circuit
from application.utils import utils
from application.services.job import Job
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
            logging.info("Getting shortest queue...")
            backend_name, qubits = utils.check_and_retrieve_shortest_queue(provider, logger=logger)
            logging.info(f'Shortest queue is {backend_name} with {qubits} jobs in the queue.')

            # Create job
            job = Job(circuit=create_first_circuit(), server=backend_name, shots=500, provider=provider)
            job.run_job()
            job.monitor_job()
            job.plot_job()
        except Exception as err:
            logger.exception(err)
        finally:
            self.logging_utils.logApplicationFinish()
            logging.shutdown()
            print("Shutdown")
