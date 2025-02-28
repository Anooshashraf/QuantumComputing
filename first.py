import qiskit

#create a quantum gate first with two qubits
circuit = qiskit.QuantumCircuit(2)

#apply hadamard gate to the circuit
circuit.h(0)

#create classical registers and allocate classical bits
creg = qiskit.ClassicalRegister(2,name='c')
circuit.add_register(creg)

#measure the qubits and store the measurement results in classical bits
circuit.measure([0,1],[creg[0],creg[1]])

#simulate the circuit
simulator = qiskit.Aer.get_backend('qasm_simulator')
result = qiskit.execute(circuit,simulator).result()

#Get the measurement
counts = result.get_counts()
print(counts)