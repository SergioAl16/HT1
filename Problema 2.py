# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
05/07/2023

Hoja de Trabajo # 1 - Problema 2
"""
from pylab import *

#Funcion para Divisores de un Numero sin Incluirlo
def suma_divisores(numero):
    """ Hace una suma entre todos los divisores del numero que ingrese el 
    usuario"""
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

#Numero Divisores igual a si mismo
def imprimir_numeros_perfectos(cantidad):
    """ Imprime los números perfectos tales que la suma de sus divisores 
    sea igual a sí mismo"""
    numeros_perfectos = []
    numero = 1
    while len(numeros_perfectos) < cantidad:
        suma = suma_divisores(numero)
        if suma == numero:
            numeros_perfectos.append(numero)
        numero += 1
    
    return numeros_perfectos

def imprimir_numeros_primos(cantidad):
    """ Imprime los números primos que el usuario desee obtener"""
    numeros_primos = []
    numero = 2
    while len(numeros_primos) < cantidad:
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(numero)
        numero += 1
    
    return numeros_primos

# Solicitar al usuario el número para la suma de divisores
numero = int(input("Ingrese un número para la suma de divisores: "))

# Solicitar al usuario la cantidad de números primos a devolver
cantidad_primos = int(input("Ingrese la cantidad de números primos a devolver: "))

# Calcular la suma de divisores y los números primos
suma = suma_divisores(numero)
numeros_perfectos = imprimir_numeros_perfectos(numero)
numeros_primos = imprimir_numeros_primos(cantidad_primos)

# Imprimir los resultados
print(f"La suma de divisores de {numero} es: {suma}")
print(f"Los primeros números perfectos son: {numeros_perfectos}")
print(f"Los primeros {cantidad_primos} números primos son: {numeros_primos}")