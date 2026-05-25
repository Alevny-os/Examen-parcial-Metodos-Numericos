import numpy as np
from scipy.interpolate import lagrange

# Datos cercanos a 1000 Hz

frecuencia_local = np.array([810, 895, 985, 1080, 1180, 1290])

impedancia_local = np.array([
    131.0, 131.3, 131.9,
    132.7, 133.8, 135.2
])

frecuencia_eval = 1000

print("\nINTERPOLACIÓN EN f = 1000 Hz\n")

# MÉTODO MATRICIAL

# Construcción de la matriz de Vandermonde
A = np.vander(frecuencia_local, increasing=True)

# Resolución del sistema A*c = b
coef = np.linalg.solve(A, impedancia_local)

# Evaluación del polinomio en 1000 Hz
vector_potencias = np.array([
    frecuencia_eval**i for i in range(len(frecuencia_local))
])

Z_matriz = np.dot(coef, vector_potencias)

print("Método matricial:")
print(f"|Z(1000)| ≈ {Z_matriz:.4f} ohm\n")

# MÉTODO DE LAGRANGE

polinomio_lagrange = lagrange(
    frecuencia_local,
    impedancia_local
)

Z_lagrange = polinomio_lagrange(frecuencia_eval)

print("Método de Lagrange:")
print(f"|Z(1000)| ≈ {Z_lagrange:.4f} ohm")