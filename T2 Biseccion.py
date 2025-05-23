# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:56:49 2025

@author: OSCAR JIMENEZ
"""
import math


def f(x):
    return 2 * x * math.cos(2 * x) - (x + 1)**2


a, b = -3, -2  
interaccion = 5   


for i in range(interaccion):
    c = (a + b) / 2  
    if f(a) * f(c) < 0:
        b = c  
    else:
        a = c  
    print(f"Iteración {i+1}: x = {c:.4f}, intervalo = [{a:.4f}, {b:.4f}]")