from typing import Optional

from qiskit import IBMQ

def healthy(imbq: IMBQ) -> Optional[str]:
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


