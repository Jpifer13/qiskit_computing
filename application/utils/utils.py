from typing import Optional

from qiskit.providers.ibmq.accountprovider import AccountProvider


def check_and_retrieve_shortest_queue(provider: AccountProvider, logger: None, simulated=False) -> Optional[tuple]:
    """
    This function checks the queues of all simulators
    """
    all_backends = []
    for backend in provider.backends():
        try:
            qubit_count = len(backend.properties().qubits)
        except:
            qubit_count = 'simulated'
            
        # Create dict with backends
        if not simulated and qubit_count != 'simulated' and qubit_count >= 5:
            all_backends.append((backend.name(), backend.status().pending_jobs))


        if logger:
            logger.info(f'{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits.')
        # print(f'{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits.')

    if len(all_backends) != 0:
        return min(all_backends, key=lambda item:item[1])
    else:
        return None
