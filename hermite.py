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

def derivative(data_points):
    #Uses the midpoint method to approximate the deriative at certain points
    
    #TODO: Implement Rutta Ketta method
    
    m = []
    #Can't use the midpoint method at the endpoints
    m.append((data_points[1][1] - data_points[0][1]) / ((data_points[1][0] - data_points[0][0])))
    for i in range(0, len(data_points) - 1):
        deriv = (data_points[i + 1][1] - data_points[i - 1][1]) / (data_points[i + 1][0] - data_points[i - 1][0])
        m.append(deriv)
        
    m.append((data_points[len(data_points) - 1][1] - data_points[len(data_points) - 2][1]) / (data_points[len(data_points) - 1][0] - data_points[len(data_points) - 2][0]))
    return m

def main(data_points):
    x = Symbol('x')
    m = derivative(data_points)
    H = 0
    for i in range(0, len(data_points)):
        L = lagrange(x, data_points, i)
        x_i = data_points[i][0]
        y_i = data_points[i][1]
        H += (1 - 2 * (x - x_i) * diff(L, x).subs(x, x_i)) * (L ** 2) * y_i
        H += (x - x_i) * (L ** 2) * m[i]
        H = lambdify(x, H, 'numpy')
    return H
    