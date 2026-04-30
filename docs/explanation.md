# Explicación del Método Numérico

La **Cuadratura Gaussiana** es una técnica de integración numérica que busca obtener resultados exactos para polinomios de un grado específico mediante una elección de los puntos de evaluación ($x_i$) y sus respectivos pesos ($w_i$).

A diferencia de otros métodos que utilizan puntos equidistantes, este método utiliza las raíces de los polinomios de Legendre para definir los puntos de colocación en el intervalo estándar $[-1, 1]$. 

Para aplicar este método a un intervalo distinto $[a, b]$, es necesario realizar un escalamiento lineal de los puntos y los pesos obtenidos.
