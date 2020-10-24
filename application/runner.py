import logging
import time

from qiskit import QuantumCircuit
from qiskit import IBMQ

from application.utils.LoggingUtils import LoggingUtils
from application.services.circuits import create_first_circuit, create_second_ciruit
from application.utils import utils
from application.services.job import Job

class Runner():

    def __init__(self, log_level=logging.INFO, console_log_level=None, application="Runner"):
        self.log_level = log_level
        self.console_log_level = console_log_level
        self.application = application
        self.circuit = None
        self.backend_name = None
        self.provider = None

        try:
            self.logging_utils = self._init_logging()
            self.logging_utils.logApplicationStart()
        except Exception as err:
            print(f"Unable to instantiate logging.\n{err}")

    
    def assign_circuit(self, circuit: QuantumCircuit):
        """
        This will take a circuit and assign it to the runner
        """
        self.circuit = circuit

    def create_and_assign_provider(self, hub: str):
        """
        Creates and assigns the provider given a hub name
        """
        self.provider = IBMQ.get_provider(hub)
    
    def create_first_example_circuit(self):
        """
        This gets the first example circuit that shows entanglement
        """
        logging.getLogger()

        logging.info("Running function: create_first_circuit.")
        self.circuit = create_first_circuit()
        logging.info(f"Here is the return circuit:\n{self.circuit}")
    
    def create_second_example_circuit(self):
        """
        This gets the second circuit that is an example of a particle in superposition
        """
        logging.getLogger()

        logging.info("Running function: create_second_ciruit.")
        self.circuit = create_second_ciruit()
        logging.info(f"Here is the return circuit:\n{self.circuit}")
    
    @staticmethod
    def find_shortest_queue(provider):
        """
        This will get you the shortest queue of a provider

        Args:
            provider ([AccountProvider]): [This is an AccountProvider instance from qiskit library]
        """
        logger = logging.getLogger()

        logging.info("Getting shortest queue...")
        backend_name, qubits = utils.check_and_retrieve_shortest_queue(provider, logger=logger)
        logging.info(f'Shortest queue is {backend_name} with {qubits} jobs in the queue.')

        return backend_name

    def run(self):
        try:
            logger = logging.getLogger()
            logging.info("Starting...")
            logging.info("Running...")
            print("Running...")

            self.create_and_assign_provider('ibm-q')

            backend_name = self.find_shortest_queue(self.provider)
            
            # Create job
            job = Job(circuit=self.circuit, server=backend_name, shots=500, provider=self.provider)
            logging.info(f'Here is the jobs circuit:\n{job.plot_ascii_job_circuit()}')
            job.run_job()
            job.monitor_job()
            job.plot_finished_job()
            
        except Exception as err:
            logger.exception(err)
        finally:
            self.logging_utils.logApplicationFinish()
            logging.shutdown()
            print("Shutdown")

    def _init_logging(self):
        """
        Initialize logging from custom logging class, LoggingUtils
        """
        timestamp = time.strftime("%Y%m%d%H%M%S")
        loggingFile = f'logs/{self.application}-{timestamp}.log'
        loggingUtils = LoggingUtils(self.application, logFile=loggingFile,
                                    fileLevel=self.log_level, consoleLevel=self.console_log_level)
        
        return loggingUtils
    