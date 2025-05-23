# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:40:52 2025

@author: OSCAR JIMENEZ
"""

import math


def f(x):
    return 8 * x * math.sin(x) * math.exp(-x) - 1


x, x1 = 0.5, -0.3  
interaccion = 5       


for i in range(interaccion):
    x2 = x1 - f(x1) * (x1 - x) / (f(x1) - f(x))  
    print(f"Iteración {i+1}: x = {x2:.4f}")
    x, x1 = x1, x2  