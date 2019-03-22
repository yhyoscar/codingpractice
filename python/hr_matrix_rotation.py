#!/bin/python3

import math
import os
import random
import re
import sys

def matrix_to_layers(matrix):
    m = len(matrix); n = len(matrix[0])
    nlayer = int(min(m,n)/2)
    layers = []
    for i in range(nlayer):
        layers.append([ matrix[i][i] ])
        for k in range(1, m-2*i-1):
            layers[-1].append(matrix[i+k][i])
        for k in range(n-2*i-1):
            layers[-1].append(matrix[m-i-1][i+k])
        for k in range(m-2*i-1):
            layers[-1].append(matrix[m-i-1-k][n-i-1])
        for k in range(n-2*i-1):
            layers[-1].append(matrix[i][n-i-1-k])
    return layers, m, n

def rotation_layers(layers, r):
    for array in layers:
        s = r % len(array)
        tmp = array[-s:]
        array[s:] = array[:-s]
        array[:s] = tmp
    return

def layers_to_matrix(layers, m, n):
    matrix = [[0 for i in range(n)] for j in range(m)]
    for i in range(len(layers)):
        for k in range(m-2*i-1):
            matrix[i+k][i] = layers[i][k]
        for k in range(n-2*i-1):
            matrix[m-i-1][i+k] = layers[i][k+m-2*i-1]
        for k in range(m-2*i-1):
            matrix[m-i-1-k][n-i-1] = layers[i][k+m-2*i-1+n-2*i-1]
        for k in range(n-2*i-1):
            matrix[i][n-i-1-k] = layers[i][k+2*(m-2*i-1)+n-2*i-1]
    return matrix

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    layers, m, n = matrix_to_layers(matrix)
    rotation_layers(layers, r)
    mrot = layers_to_matrix(layers, m, n)
    for i in range(m):
        for j in range(n):
            print(mrot[i][j], end=' ')
        print('')
    return

if __name__ == '__main__':
    mnr = input().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
