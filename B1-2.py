import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import random
# Datos experimentales

f = np.array([
    100,120,145,170,200,235,270,310,355,405,
    460,520,585,655,730,810,895,985,1080,1180,
    1290,1410,1540,1680,1830,1990,2160,2340,2530,2730
])

Z = np.array([
    152.3,149.1,146.8,144.9,142.0,139.5,137.9,136.1,
    134.8,133.6,132.7,131.9,131.4,131.1,130.9,131.0,
    131.3,131.9,132.7,133.8,135.2,136.9,138.9,141.1,
    143.5,146.1,149.0,152.2,155.6,159.2
])

# Comparación de distintos grados

x = np.linspace(100, 2730, 1200)

# Polinomios locales
P5 = lagrange(f[12:18], Z[12:18])

P10 = lagrange(f[10:21], Z[10:21])

P15 = lagrange(f[7:23], Z[7:23])

# Polinomio global
P29 = lagrange(f, Z)

plt.figure(figsize=(10,5))

plt.scatter(f, Z, color='black', label='Datos')

plt.plot(x, P5(x), '--', label='Grado 5')

plt.plot(x, P10(x), '-.', label='Grado 10')

plt.plot(x, P15(x), ':', label='Grado 15')

plt.plot(
    x,
    P29(x),
    color='red',
    alpha=0.6,
    label='Grado 29'
)

plt.title('Fenómeno de Runge en interpolación polinómica')

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|Z| [Ω]')

plt.ylim(120,170)

plt.grid(True, linestyle=':')

plt.legend()

plt.show()

# Estimación en 1000 Hz

valor_1000 = P5(1000)

print("\nInterpolación usando polinomio grado 5")
print(f"|Z(1000)| ≈ {valor_1000:.4f} ohm")

# VALIDACIÓN LOO

random.seed(21)

puntos_test = random.sample(range(5,25), 5)

lista_errores = []

print("\nVALIDACIÓN LEAVE-ONE-OUT\n")

for k in puntos_test:

    frecuencia_real = f[k]

    Z_real = Z[k]

    # Eliminación temporal del punto
    f_aux = np.delete(f, k)

    Z_aux = np.delete(Z, k)

    # Selección local de puntos cercanos
    indices = np.argsort(
        np.abs(f_aux - frecuencia_real)
    )[:6]

    # Nuevo polinomio local
    P_local = lagrange(
        f_aux[indices],
        Z_aux[indices]
    )

    # Predicción
    Z_interp = P_local(frecuencia_real)

    # Error relativo porcentual
    error = abs(
        (Z_real - Z_interp) / Z_real
    ) * 100

    lista_errores.append(error)

    print(f"f = {frecuencia_real} Hz")
    print(f"Error = {error:.4f}%\n")

# Promedio final
print("Error relativo promedio:")
print(f"{np.mean(lista_errores):.4f}%")