#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:12:43 2020

@author: matteo
"""

from sympy import Symbol, diff
from sympy.utilities.lambdify import lambdify


def lagrange(x, data_points, i):
    P = 1
    for j in range(0, len(data_points)):
        if j != i:
            P *= (x - data_points[j][0]) / (data_points[i][0] - data_points[j][0])
            
    return P
    
def main(data_points):
    x = Symbol('x')
    polynomial = 0
    for i in range(0, len(data_points)):
        L = lagrange(x, data_points, i)
        polynomial += L * data_points[i][1]
        L = lambdify(x, L, 'numpy')
    return L
    
