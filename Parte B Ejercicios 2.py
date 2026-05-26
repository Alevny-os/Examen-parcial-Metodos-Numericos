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

# PASO ENTRE DATOS

h = 2.5

# DIFERENCIA CENTRADA ORDEN 2

def derivada_centrada_2(fx_m1, fx_p1, h):

    return (fx_p1 - fx_m1)/(2*h)

# DIFERENCIA CENTRADA ORDEN 4

def derivada_centrada_4(fx_m2, fx_m1, fx_p1, fx_p2, h):

    return (-fx_p2 + 8*fx_p1 - 8*fx_m1 + fx_m2)/(12*h)

# DIFERENCIA PROGRESIVA ORDEN 2

def derivada_progresiva_2(fx0, fx1, fx2, h):

    return (-3*fx0 + 4*fx1 - fx2)/(2*h)

# DERIVADAS EN f = 40 kHz

dV40_o2 = derivada_centrada_2(
    1.048,
    0.689,
    h
)

dV40_o4 = derivada_centrada_4(
    1.216,
    1.048,
    0.689,
    0.521,
    h
)

# DERIVADAS EN f = 70 kHz

dV70_o2 = derivada_centrada_2(
    0.096,
    0.318,
    h
)

dV70_o4 = derivada_centrada_4(
    0.018,
    0.096,
    0.318,
    0.452,
    h
)

# DERIVADAS EN f = 100 kHz

dV100_o2 = derivada_centrada_2(
    0.894,
    0.954,
    h
)

dV100_o4 = derivada_centrada_4(
    0.856,
    0.894,
    0.954,
    1.004,
    h
)

# DERIVADA PROGRESIVA EN 10 kHz

dV10_prog = derivada_progresiva_2(
    0.842,
    0.911,
    0.986,
    h
)

# SPLINE CÚBICO

spline_V = CubicSpline(f, V, bc_type='natural')

# DERIVADAS DEL SPLINE

dSpline40 = spline_V.derivative()(40)
dSpline70 = spline_V.derivative()(70)
dSpline100 = spline_V.derivative()(100)
dSpline10 = spline_V.derivative()(10)

# RESULTADOS

print("PARTE 2 - DERIVACIÓN NUMÉRICA\n")

print("Derivadas en f = 40 kHz")
print(f"Orden 2      : {dV40_o2:.6f}")
print(f"Orden 4      : {dV40_o4:.6f}")
print(f"Spline       : {dSpline40:.6f}")

print()

print("Derivadas en f = 70 kHz")
print(f"Orden 2      : {dV70_o2:.6f}")
print(f"Orden 4      : {dV70_o4:.6f}")
print(f"Spline       : {dSpline70:.6f}")

print()

print("Derivadas en f = 100 kHz")
print(f"Orden 2      : {dV100_o2:.6f}")
print(f"Orden 4      : {dV100_o4:.6f}")
print(f"Spline       : {dSpline100:.6f}")

print()

print("Derivada progresiva en f = 10 kHz")
print(f"Orden 2      : {dV10_prog:.6f}")
print(f"Spline       : {dSpline10:.6f}")

# INTERPRETACIÓN

print("\nInterpretación física:\n")

print("Una derivada positiva indica que el")
print("voltaje aumenta con la frecuencia.")

print()

print("Una derivada negativa indica que el")
print("voltaje disminuye con la frecuencia.")

print()

print("Valores grandes de derivada representan")
print("mayor sensibilidad del front-end.")