import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Datos experimentales

frecuencia = np.array([
    100,120,145,170,200,235,270,310,355,405,
    460,520,585,655,730,810,895,985,1080,1180,
    1290,1410,1540,1680,1830,1990,2160,2340,
    2530,2730
])

impedancia = np.array([
    152.3,149.1,146.8,144.9,142.0,139.5,137.9,
    136.1,134.8,133.6,132.7,131.9,131.4,131.1,
    130.9,131.0,131.3,131.9,132.7,133.8,135.2,
    136.9,138.9,141.1,143.5,146.1,149.0,152.2,
    155.6,159.2
])

# Construcción del spline

spline = CubicSpline(
    frecuencia,
    impedancia,
    bc_type='natural'
)

# Primera derivada analítica
primera_derivada = spline.derivative(1)

# Evaluación en los puntos originales

dZ_df = primera_derivada(frecuencia)

# Búsqueda del cambio de signo

ceros = primera_derivada.roots()

# Filtramos raíces dentro del intervalo
frecuencia_min = [
    r for r in ceros
    if 100 <= r <= 2730
][0]

# Malla fina para gráfica suave

x = np.linspace(100, 2730, 1200)

y = primera_derivada(x)

# Gráfica

plt.figure(figsize=(10,5))

# Curva derivada
plt.plot(
    x,
    y,
    linewidth=2,
    label='d|Z|/df'
)

# Puntos calculados
plt.scatter(
    frecuencia,
    dZ_df,
    color='black',
    s=25,
    label='Valores evaluados'
)

# Línea horizontal y = 0
plt.axhline(
    0,
    linestyle='--',
    linewidth=1
)

# Punto donde cambia el signo
plt.scatter(
    frecuencia_min,
    0,
    color='red',
    s=70,
    label='Cambio de signo'
)

plt.title('Primera derivada de la impedancia')

plt.xlabel('Frecuencia [Hz]')

plt.ylabel('d|Z|/df [Ω/Hz]')

plt.grid(True, linestyle=':')

plt.legend()

plt.show()

# Resultado final

print("\nRESULTADO DEL MÍNIMO\n")

print(
    f"La derivada cambia de negativa "
    f"a positiva en f ≈ {frecuencia_min:.4f} Hz"
)