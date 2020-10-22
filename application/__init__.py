from qiskit import IBMQ
from .runner import Runner

def create_app():
    # Check if account is currently loaded and if it isn't create one
    if not IBMQ.active_account:
        IBMQ.save_account('MY_API_TOKEN')

    runner = Runner()

    return runner