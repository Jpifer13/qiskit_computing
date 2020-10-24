
import qiskit as q
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from matplotlib import style

class Job():
    def __init__(self, provider, circuit, server: str, shots: int, name: str = None):
        self.provider = provider
        self.circuit = circuit
        self.server = server
        self.shots = shots
        self.name = name
        self.job = None
        self.result = None
    
    def _get_backend(self):
        return self.provider.get_backend(self.server)
    
    def run_job(self):
        self.job = q.execute(experiments=self.circuit, backend=self._get_backend(), shots=self.shots)
        return self.job
    
    def monitor_job(self):
        if self.job:
            job_monitor(self.job)
            self.result = self.job.result()
        else:
            return None
    
<<<<<<< HEAD
    def plot_ascii_job_circuit(self):
        return self.circuit.draw()

    def plot_finished_job(self):
=======
    def plot_job(self):
>>>>>>> develop
        style.use('dark_background')

        counts = self.result.get_counts(self.circuit)

        plot_histogram([counts])
        plt.show()
