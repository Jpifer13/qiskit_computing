import matplotlib.pyplot as plt
import qiskit as q


def create_first_circuit() -> q.QuantumCircuit:
    circuit = q.QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits

    # currently: 0, 0
    circuit.x(0)  # Not gate. Think of this as 1, 0... x=True, y=False so x=y False

    circuit.cx(0, 1)  # cnot, controlled not. Flips 2nd qubit value IF and only if 1st qubit is a 1
    # So now what we should have is a 1, 1

    # Know that before measure if qubits are in superposition, meaning the qubits are in every posistion,
    # when we take this measurement the fall out of superposition because they are now observed
    circuit.measure([0, 1], [0, 1])  # classify how the qubit register is going to map to the classical register
    # So what the above line means is that we take the qubit at index 0 and map it to the classical index 0
    # and the same with the second. I think this needs to be done because a qubit holds more "indeces" then 
    # the classical bit so we need to define, or map, it how we want. So this acts as a translater between quantum
    # language and python

    # ascii_image = circuit.draw()  # This will give an ascii representation of the circuit
    # print(ascii_image)

    # circuit.draw(output='mpl')  # This makes the output using matplotlib
    # plt.show()

    return circuit


