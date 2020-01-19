import numpy as numpy
from random import *

#checks if the current coordinate location meets conditions according to sudoku rules
def istrue(arr,i,j):
    ans = True
    for i2 in range(0,9):
        if arr[i2][j] == arr[i][j] and i2 != i:
            ans = False
    for j2 in range(0,9):
        if arr[i][j2] == arr[i][j] and j2 != j:
            ans = False
    nonet_y = j // 3
    nonet_x = i // 3
    for i3 in range(nonet_x * 3, nonet_x * 3 + 3):
        for j3 in range(nonet_y * 3, nonet_y * 3 + 3):
            if arr[i3][j3] == arr[i][j] and (i3 != i and j3 != j):
                ans = False
    return ans
# finds a valid coordinate that is empty and can be used by the backtracking function
def validspot(arr):
    for i in range(0,9):
        for j in range(0,9):
            if arr[i][j] == 0:
                return (i,j)
    return False
#carries out the backtracking algorithm to solve the sodoku board
def backtrack(arr):
    if validspot(arr) == False:
        return 'done'
    i = validspot(arr)[0]
    j = validspot(arr)[1]
    for x in range(1,10):
        arr[i][j] = x
        if istrue(arr,i,j) == True:
            y = backtrack(arr)
            if y == 'done':
                return 'done'
            
    arr[i][j] = 0
    return False

    



    

