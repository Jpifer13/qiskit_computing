import os
from qiskit import IBMQ
from .runner import Runner

def create_app():
    account = None
    try:
        account = IBMQ.load_account()
    except Exception as err:
        print(f'No account available to load. Error: {err}')
        
    # Check if account is currently loaded and if it isn't create one
    if not account:
        IBMQ.save_account(str(os.getenv('QISKIT_TOKEN')), overwrite=True)
        IBMQ.load_account()
    else:
        print(f'You are logged in with this info: {account}')

    runner = Runner()

    return runner