# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
05/07/2023

Hoja de Trabajo # 1 - Problema 3
"""
from pylab import *
#Funcion para Contar los Multiplos con FOR
def contar_multiplos_for(numero1, numero2):
    """Cuenta uántos múltiplos hay del primer numero ingresado"""
    contador = 0
    for i in range(numero1, numero2):
        if i % numero1 == 0:
            contador += 1
    return contador

#Funcion para Contar los Multiplos con WHILE
def contar_multiplos_while(numero1, numero2):
    """Ve cuales de los multiplos del primer numero son menores al segundo"""
    contador = 0
    multiplo = numero1
    while multiplo < numero2:
        contador += 1
        multiplo += numero1
    return contador

# Solicitar al usuario los dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Utilizar la función contar_multiplos_for
cantidad_for = contar_multiplos_for(numero1, numero2)
print(f"Utilizando ciclo for, hay {cantidad_for} múltiplos de {numero1} menores que {numero2}.")

# Utilizar la función contar_multiplos_while
cantidad_while = contar_multiplos_while(numero1, numero2)
print(f"Utilizando ciclo while, hay {cantidad_while} múltiplos de {numero1} menores que {numero2}.")
