from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

circuit = QuantumCircuit(2)

circuit.h(0)
circuit.cx(0,1)
circuit.draw()
