# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:28:53 2025

@author: OSCAR JIMENEZ
"""
n = input("Introduce un número: ")

try:
    n = int(n)
    if n > 0:
        print("El número es entero y positivo.")
    else:
        print("Error: el número debe ser positivo.")
except:
    print("Error: debes ingresar un número entero.")

