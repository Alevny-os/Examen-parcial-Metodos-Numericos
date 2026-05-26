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

Z = np.array([
182.4,178.9,175.1,171.0,166.8,162.7,158.9,155.4,152.0,149.0,
146.1,145.2,145.8,147.3,149.9,153.5,158.0,163.2,168.9,174.8,
180.5,186.2,191.5,196.2,200.1,203.1,205.2,206.3,206.1,204.7,
198.0,194.4,190.9,187.8,185.1,183.0,181.6,180.8,180.6,180.9
])

# FUNCIÓN DE LAGRANGE DE SEGUNDO GRADO

def lagrange2(x, x0, y0, x1, y1, x2, y2):

    L0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
    L1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    L2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))

    P = y0*L0 + y1*L1 + y2*L2

    return P

# INTERPOLACIÓN DE LAGRANGE

# ---- V(41) ----

V_41 = lagrange2(
    41,
    37.5, 1.048,
    40.0, 0.866,
    42.5, 0.689
)

# ---- Z(41) ----

Z_41 = lagrange2(
    41,
    37.5, 145.2,
    40.0, 145.8,
    42.5, 147.3
)

# ---- V(73) ----

V_73 = lagrange2(
    73,
    70.0, 0.197,
    72.5, 0.318,
    75.0, 0.452
)

# ---- Z(73) ----

Z_73 = lagrange2(
    73,
    70.0, 200.1,
    72.5, 203.1,
    75.0, 205.2
)

# RESULTADOS LAGRANGE

print("\nINTERPOLACIÓN DE LAGRANGE\n")

print(f"V(41 kHz)  = {V_41:.6f} V")
print(f"|Z|(41 kHz)= {Z_41:.6f} Ohm")

print()

print(f"V(73 kHz)  = {V_73:.6f} V")
print(f"|Z|(73 kHz)= {Z_73:.6f} Ohm")

# SPLINE CÚBICO NATURAL

spline_V = CubicSpline(f, V, bc_type='natural')
spline_Z = CubicSpline(f, Z, bc_type='natural')

# EVALUACIÓN DEL SPLINE

V41_spline = spline_V(41)
Z41_spline = spline_Z(41)

V73_spline = spline_V(73)
Z73_spline = spline_Z(73)

# RESULTADOS SPLINE

print("\nSPLINE CÚBICO NATURAL\n")

print(f"V(41 kHz)  = {V41_spline:.6f} V")
print(f"|Z|(41 kHz)= {Z41_spline:.6f} Ohm")

print()

print(f"V(73 kHz)  = {V73_spline:.6f} V")
print(f"|Z|(73 kHz)= {Z73_spline:.6f} Ohm")

# COMPARACIÓN

print("\nCOMPARACIÓN\n")

print("El spline cúbico genera una aproximación")
print("más suave y estable que Lagrange.")
print("Además evita oscilaciones excesivas")
print("cuando existen muchos datos experimentales.")