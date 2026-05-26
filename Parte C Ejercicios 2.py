import numpy as np
from scipy.interpolate import CubicSpline

# DATOS DEL ENSAYO

f = np.array([
10.0,12.5,15.0,17.5,20.0,22.5,25.0,27.5,30.0,32.5,
35.0,37.5,40.0,42.5,45.0,47.5,50.0,52.5,55.0,57.5,
60.0,62.5,65.0,67.5,70.0,72.5,75.0,77.5,80.0,82.5,
85.0,87.5,90.0,92.5,95.0,97.5,100.0,102.5,105.0,107.5
])

V = np.array([
0.842,0.911,0.986,1.062,1.143,1.227,1.314,1.401,1.482,1.551,
1.216,1.048,0.866,0.689,0.521,0.364,0.223,0.103,0.012,-0.041,
-0.057,-0.034,0.018,0.096,0.197,0.318,0.452,0.579,0.700,0.809,
0.611,0.688,0.756,0.811,0.856,0.894,0.926,0.954,0.980,1.004
])

# IDENTIFICACIÓN DEL CAMBIO DE SIGNO

print("PARTE 3 - RAÍCES POR BISECCIÓN\n")

for i in range(len(V)-1):

    if V[i] * V[i+1] < 0:

        print("Cambio de signo encontrado:")
        print(f"Intervalo = [{f[i]}, {f[i+1]}]")
        print(f"V({f[i]}) = {V[i]}")
        print(f"V({f[i+1]}) = {V[i+1]}")
        print()

# MÉTODO DE BISECCIÓN

def biseccion(func, a, b, tol=1e-6, max_iter=100):

    for i in range(max_iter):

        c = (a + b)/2

        if func(a)*func(c) < 0:
            b = c
        else:
            a = c

        if abs(func(c)) < tol:
            break

    return c

# SPLINE CÚBICO

spline_V = CubicSpline(f, V, bc_type='natural')

# PRIMERA RAÍZ

a1 = 55.0
b1 = 57.5

raiz1 = biseccion(spline_V, a1, b1)

# SEGUNDA RAÍZ

a2 = 62.5
b2 = 65.0

raiz2 = biseccion(spline_V, a2, b2)

# RESULTADOS

print("Primera raíz")
print(f"Intervalo inicial : [{a1}, {b1}]")
print(f"Raíz aproximada   : {raiz1:.6f} kHz")

print()

print("Segunda raíz")
print(f"Intervalo inicial : [{a2}, {b2}]")
print(f"Raíz aproximada   : {raiz2:.6f} kHz")

# COMPARACIÓN

print("\nComparación:\n")

print("El método de bisección permite")
print("localizar las raíces de manera estable.")

print()

print("El spline cúbico mejora la precisión")
print("debido a la suavidad de la interpolación.")