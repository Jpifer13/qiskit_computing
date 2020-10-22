from application import create_app
import qiskit

App = create_app()

if __name__ == '__main__':
    print(f"Qiskit versions: {qiskit.__qiskit_version__}")
    App.run()
