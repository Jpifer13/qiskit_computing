import qiskit
from application import create_app
from application.services.circuits import create_first_circuit, create_second_ciruit

App = create_app()

if __name__ == '__main__':
    print(f"Qiskit versions: {qiskit.__qiskit_version__}")
    App.create_first_example_circuit()
    App.run()
