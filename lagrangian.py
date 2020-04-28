#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:12:43 2020

@author: matteo
"""

from sympy import *
from sympy.utilities.lambdify import lambdify
import sys
from csv import reader
import matplotlib.pyplot as plt
import numpy as np

def lagrange(x, data_points, i):
    P = 1
    for j in range(0, len(data_points)):
        if j != i:
            P *= (x - data_points[j][0]) / (data_points[i][0] - data_points[j][0])
            
    return P
    
def main(data_points, file):
    x = Symbol('x')
    polynomial = 0
    for i in range(0, len(data_points)):
        L = lagrange(x, data_points, i)
        polynomial += L * data_points[i][1]
    f = open(file, 'w')
    f.write(str(polynomial))
    f.close()
    L = lambdify(x, polynomial, 'numpy')
    return L
    
if __name__ == '__main__':
    file = sys.argv[1]
    data = np.array([])
    with open(file, 'r') as csvfile:
        csvreader = reader(csvfile, delimiter=',')
        for row in csvreader:
            data = np.append(data, row, axis = 0)

    #The negative -1 allows the reshape function to determine the number of columns
    data = np.reshape(data, (2, -1))
    data = data.T
    data = data.astype(float)
    x = data[:, 0]
    y = data[:, 1]
    H = main(data, sys.argv[2])
    plt.scatter(x, y)
    plt.plot(x, H(x))
    plt.show()
