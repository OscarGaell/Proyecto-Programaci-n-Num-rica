# -*- coding: utf-8 -*-
"""
Created on Fri Feb 7 18:15:54 2025

@author: OSCAR JIMENEZ
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
plt.plot(x, x**2, label="x^2")
plt.plot(x, x**3, label="x^3")
plt.plot(x, x, label="x")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Funciones x^2, x^3 y x")
plt.legend()
plt.grid(True)
plt.show()