try:
    from qiskit import  QuantumCircuit 
    print("Qiskit is installed successfully.")
except ImportError as e:
    print(f"ImportError: {e}")
