# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:20:29 2025

@author: OSCAR JIMENEZ
"""

import math


def f(x):
    return 8 * x * math.sin(x) * math.exp(-x) - 1

def df(x):
    return 8 * math.sin(x) * math.exp(-x) + 8 * x * math.cos(x) * math.exp(-x) - 8 * x * math.sin(x) * math.exp(-x)


x = 0.3      
interaccion = 5   


for i in range(interaccion):
    x1 = x - f(x) / df(x)  
    print(f"Iteración {i+1}: x = {x1:.4f}")
    x = x1  