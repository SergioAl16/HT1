# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
06/07/2023

Hoja de Trabajo # 1 - Problema 6
"""
from pylab import *

#Creacion de Matrices
def operacion_matrices(matriz1, matriz2, operacion):
    """Muestra el resultado entre la suma o producto de 2 matricez que el
    usuario las puede cambiar editando el codigo y si no se puede realizar la 
    suma o producto envia un mensaje de ERROR"""
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])

    # Verificar si las matrices son compatibles para la operación
    if operacion == 'suma' and (filas1 != filas2 or columnas1 != columnas2):
        return "Incompatibles para la suma."
    elif operacion == 'producto' and columnas1 != filas2:
        return "Incompatibles para el producto."

    # Realizar la operación correspondiente
    if operacion == 'suma':
        resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas1)] for i in range(filas1)]
    elif operacion == 'producto':
        resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(columnas1)) for j in range(columnas2)] for i in range(filas1)]
    
    return resultado

""" SE DEBE EDITAR ESTAS VARIABLES PARA QUE TRABAJE LA FUNCION"""
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [3, 5, 8]]
operacion = 'suma' #se puede cambiar entre "suma" o "producto"
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


# Realizar la operación entre las matrices
resultado = operacion_matrices(matriz1, matriz2, operacion)

# Imprimir el resultado
print(f"La Matriz es: {resultado}")
