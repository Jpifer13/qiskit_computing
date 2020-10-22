from typing import Optional

from qiskit.providers.ibmq.accountprovider import AccountProvider

def healthy(imbq) -> Optional[str]:
    """
    This is a health check service that when called will return whether or not 
    the connection to qiskit services is working

    Args:
        imbq (IMBQ): IMBQ object
    Returns:
        str: Healthy statement
        None: no connection
    """
    pass

def check_queues(provider: AccountProvider, logger: None):
    """
    This function checks the queues of all simulators
    """
    for backend in provider.backends():
        try:
            qubit_count = len(backend.properties().quibits)
        except:
            qubit_count = 'simulated'

        if logger:
            logger.info(f'{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits.')
        print(f'{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits.')


