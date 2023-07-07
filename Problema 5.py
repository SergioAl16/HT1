# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
06/07/2023

Hoja de Trabajo # 1 - Problema 5
"""
from pylab import *

#Funcion de Empaquetar
def empaquetar(lista):
    """Crea una matriz en la que, en la primera parte muestra el numero y en la
    segunda, la cantidad que se repite ese numero, entoces la funcion cuenta
    en un FOR cuantas veces sale ese numero"""
    empaquetado = []
    cantidad = 0
    elemento_actual = None
    
    for elemento in lista:
        if elemento == elemento_actual:
            cantidad += 1
        else:
            if elemento_actual is not None:
                empaquetado.append((elemento_actual, cantidad))
            elemento_actual = elemento
            cantidad = 1
    
    if elemento_actual is not None:
        empaquetado.append((elemento_actual, cantidad))
    
    return empaquetado

""" SE DEBE EDITAR ESTAS VARIABLES PARA QUE TRABAJE LA FUNCION"""
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
lista = [1, 1, 1, 3, 5, 1, 1, 3, 3]
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
resultado = empaquetar(lista)
print(f"Numero - Cant. de Repeticiones: {resultado}")