# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:20:02 2025

@author: OSCAR JIMENEZ
"""

import random

n = int(input("introduce un número entero y positivo: "))

if n > 0:
    v = [random.randint(1, 9) for _ in range(n)]
    print("vector generado:", v)
    m = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(v[j] * (i + 1))
        m.append(fila)
    for f in m:
        print(f)
else:
    print("error: el número debe ser entero y positivo.")
