import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, lagrange

# Datos experimentales

frecuencia = np.array([
    100,120,145,170,200,235,270,310,355,405,
    460,520,585,655,730,810,895,985,1080,1180,
    1290,1410,1540,1680,1830,1990,2160,2340,2530,2730
])

impedancia = np.array([
    152.3,149.1,146.8,144.9,142.0,139.5,137.9,
    136.1,134.8,133.6,132.7,131.9,131.4,131.1,
    130.9,131.0,131.3,131.9,132.7,133.8,135.2,
    136.9,138.9,141.1,143.5,146.1,149.0,152.2,
    155.6,159.2
])

# Construcción del spline cúbico natural

spline = CubicSpline(
    frecuencia,
    impedancia,
    bc_type='natural'
)

# Polinomio local usado en la parte B1

indices = np.where(
    (frecuencia >= 810) &
    (frecuencia <= 1290)
)[0]

P_local = lagrange(
    frecuencia[indices],
    impedancia[indices]
)

# Mallas para visualización

x_global = np.linspace(100, 2730, 1200)

x_local = np.linspace(500, 1600, 400)

# Evaluación de funciones
y_spline = spline(x_global)

y_local = P_local(x_local)

# Gráfica comparativa

plt.figure(figsize=(10,5))

# Datos originales
plt.scatter(
    frecuencia,
    impedancia,
    color='black',
    label='Datos experimentales'
)

# Spline cúbico
plt.plot(
    x_global,
    y_spline,
    linewidth=2,
    label='Spline cúbico natural'
)

# Polinomio local
plt.plot(
    x_local,
    y_local,
    '--',
    linewidth=2,
    label='Polinomio local grado 5'
)

plt.title('Comparación entre spline y polinomio local')

plt.xlabel('Frecuencia [Hz]')

plt.ylabel('|Z| [Ω]')

plt.xlim(400,1700)

plt.ylim(130,145)

plt.grid(True, linestyle=':')

plt.legend()

plt.show()

# Evaluación en 1000 Hz

Z_spline = spline(1000)

Z_polinomio = P_local(1000)

diferencia = abs(Z_spline - Z_polinomio)

print("\nRESULTADOS EN 1000 Hz\n")

print(f"Spline cúbico      : {Z_spline:.4f} ohm")

print(f"Polinomio grado 5  : {Z_polinomio:.4f} ohm")

print(f"Diferencia absoluta: {diferencia:.4f} ohm")