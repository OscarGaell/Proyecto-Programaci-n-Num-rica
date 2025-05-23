# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:56:09 2025

@author: OSCAR JIMENEZ
"""
from random import randint

n = int(input("introduce un número entero y positivo: "))

if n > 0:
    v = []
    for i in range(n):
        v.append(randint(1, 9))
    print("vector generado:", v)
else:
    print("error: el número debe ser entero y positivo.")