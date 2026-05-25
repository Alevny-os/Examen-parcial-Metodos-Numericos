import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales

# Frecuencia de excitación (Hz)
frecuencia = np.array([
    100, 120, 145, 170, 200, 235, 270, 310, 355, 405,
    460, 520, 585, 655, 730, 810, 895, 985, 1080, 1180,
    1290, 1410, 1540, 1680, 1830, 1990, 2160, 2340, 2530, 2730
])

# Magnitud de impedancia medida (Ohm)
impedancia = np.array([
    152.3, 149.1, 146.8, 144.9, 142.0, 139.5, 137.9, 136.1, 134.8,
    133.6, 132.7, 131.9, 131.4, 131.1, 130.9, 131.0, 131.3, 131.9,
    132.7, 133.8, 135.2, 136.9, 138.9, 141.1, 143.5, 146.1, 149.0,
    152.2, 155.6, 159.2
])

# Búsqueda del mínimo experimental

indice_minimo = np.argmin(impedancia)

f_min = frecuencia[indice_minimo]
z_min = impedancia[indice_minimo]

print("Frecuencia aproximada del mínimo:")
print(f"{f_min:.4f} Hz")

print("\nValor mínimo de impedancia:")
print(f"{z_min:.4f} ohm")

# Construcción de la gráfica

plt.figure(figsize=(10,6))

# Curva principal de datos
plt.plot(
    frecuencia,
    impedancia,
    'o--',
    color='navy',
    linewidth=1.8,
    markersize=6,
    label='Datos experimentales'
)

# Punto mínimo resaltado
plt.scatter(
    f_min,
    z_min,
    color='crimson',
    s=90,
    label='Mínimo local'
)

# Texto informativo del mínimo
plt.annotate(
    f'({f_min:.0f} Hz , {z_min:.1f} Ω)',
    xy=(f_min, z_min),
    xytext=(f_min+150, z_min+3),
    arrowprops=dict(arrowstyle='->')
)

# Configuración visual
plt.title('Comportamiento de la impedancia respecto a la frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|Z| [Ω]')

plt.grid(True, linestyle=':', alpha=0.8)
plt.legend()

# Mostrar resultado final
plt.show()