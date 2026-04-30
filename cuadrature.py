"""
Módulo para calcular integrales usando Cuadratura Gaussiana.

Este módulo provee las funciones necesarias para calcular
puntos de colocación, escalar intervalos y evaluar la integral
de una función específica utilizando el método de Cuadratura Gaussiana.
"""

from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    """
    Calcula los puntos de colocación y pesos para la cuadratura Gaussiana.

    Args:
        N (int): El número de puntos de integración.

    Returns:
        tuple: Un par (x, w) donde 'x' son los puntos de colocación 
        y 'w' son los pesos correspondientes en el intervalo [-1, 1].

    Example:
        >>> x, w = gaussxw(3)
        >>> print(x)
        [-0.77459667  0.          0.77459667]
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """
    Escala los puntos y pesos del intervalo estándar [-1, 1] al intervalo [a, b].

    Args:
        a (float): Límite inferior del nuevo intervalo.
        b (float): Límite superior del nuevo intervalo.
        x (array): Arreglo de puntos de colocación originales.
        w (array): Arreglo de pesos originales.

    Returns:
        tuple: Un par (x_scaled, w_scaled) con los puntos y pesos 
        escalados al nuevo intervalo [a, b].

    Example:
        >>> x, w = gaussxw(2)
        >>> x_s, w_s = gaussxwab(0, np.pi, x, w)
    """
    x_scaled = 0.5 * (b - a) * x + 0.5 * (b + a)
    w_scaled = 0.5 * (b - a) * w
    return x_scaled, w_scaled

def func(varInd):
    """
    Define la función matemática a integrar.
    
    En este caso, la función es sin(x^2).

    Args:
        varInd (float o array): La variable independiente (x).

    Returns:
        float o array: El valor de la función evaluada en 'varInd'.

    Example:
        >>> y = func(np.sqrt(np.pi/2))
        >>> print(y)
        1.0
    """
    return np.sin(varInd**2)


# ==========================================
# CÁLCULO Y GRAFICACIÓN
# ==========================================

N_min = 2
N_max = 50

# Se calcula la cantidad de valores de N y resultados de la integral.
valores_N = np.arange(N_min, N_max + 1)
cantidad_n = N_max - N_min + 1

# Se crea un arreglo de resultados.
resultados = np.zeros(cantidad_n)

# El ciclo pasa por cada valor de N.
for i in range(cantidad_n):
    N_actual = valores_N[i]
    
    # Se calculan los x y w.
    x, w = gaussxw(N_actual)
    
    # Se escalan los x y w al rango solicitado.
    x_scaled, w_scaled = gaussxwab(0.0, np.pi, x, w)
    
    # Se calcula el valor de la integral para cada N.
    resultados[i] = np.sum(w_scaled * func(x_scaled))

# Se grafica el valor de la integral en función de N.
plt.figure(figsize=(8,5))
plt.plot(valores_N, resultados, marker='.', linestyle='-')

plt.title('Convergencia de la integral $I = \int_0^\pi \sin(x^2) dx$')
plt.xlabel('Número de puntos ($N$)')
plt.ylabel('Valor de la integral')
plt.grid(True)
# plt.show() # Comentado para que no detenga MkDocs al ejecutarse
