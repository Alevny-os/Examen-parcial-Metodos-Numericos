import numpy as np
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

# Construcción del spline cúbico

spline = CubicSpline(
    frecuencia,
    impedancia,
    bc_type='natural'
)

# Nivel crítico
Z_limite = 150

# Función objetivo
def F(x):
    return spline(x) - Z_limite

# Derivada del spline
def dF(x):
    return spline.derivative(1)(x)

# MÉTODO DE BISECCIÓN

def metodo_biseccion(a, b, tolerancia=1e-6):

    contador = 0

    while abs(b - a) > tolerancia:

        punto_medio = (a + b) / 2

        if F(a) * F(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio

        contador += 1

    return (a + b) / 2, contador

# MÉTODO DE NEWTON-RAPHSON

def metodo_newton(x0, tolerancia=1e-6):

    x = x0

    iteraciones = 0

    while True:

        x_nuevo = x - F(x) / dF(x)

        iteraciones += 1

        if abs(x_nuevo - x) < tolerancia:
            break

        x = x_nuevo

    return x_nuevo, iteraciones

# Primera raíz

raiz1_bis, n1_bis = metodo_biseccion(100, 120)

raiz1_newton, n1_newton = metodo_newton(110)

# Segunda raíz

raiz2_bis, n2_bis = metodo_biseccion(2100, 2400)

raiz2_newton, n2_newton = metodo_newton(2200)

# Sensibilidad df/dZ

sensibilidad = 1 / dF(raiz2_newton)

# Resultados

print("\nRESULTADOS DE LAS RAÍCES\n")

print(f"Raíz inferior ≈ {raiz1_newton:.4f} Hz")
print(f"Bisección: {n1_bis} iteraciones")
print(f"Newton-Raphson: {n1_newton} iteraciones\n")

print(f"Raíz superior ≈ {raiz2_newton:.4f} Hz")
print(f"Bisección: {n2_bis} iteraciones")
print(f"Newton-Raphson: {n2_newton} iteraciones\n")

print(f"Sensibilidad df/d|Z| ≈ {sensibilidad:.4f} Hz/ohm")