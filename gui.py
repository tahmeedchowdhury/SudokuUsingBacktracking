from tkinter import *
from tkinter import simpledialog
import numpy as numpy
from main import istrue
from tkinter import messagebox
from main import validspot
import time as time
root = Tk()
root.geometry('720x700')
root.title('Sudoku Solver(Bactracking Algorithm)')
arr = numpy.zeros((9,9))

storage = []
class cube:
    def __init__(self,arr,i,j):
        self.i = i
        self.j = j
        self.text = str(arr[i][j])
        self.button = Button(root,text= self.text,command= lambda: cube.onclick(self))

    def onclick(self):
        x = simpledialog.askinteger("Selection Message","Choose a number from 1 to 9")
        self.button["text"] = str(x)
        arr[self.i][self.j] = x

for i in range(0,9):
    storage.append([])
    for j in range(0,9):
        b = cube(arr,i,j)
        storage[i].append(b)
        b.button.place(y = i * 50, x = j * 80, width = 80, height = 50)

def check_board(arr):
    for i in range(0,9):
        for j in range(0,9):
            if istrue(arr,i,j) == False:
                messagebox.showinfo('Message', 'Sorry but your answer is not correct! Try Again!')
                return False
    messagebox.showinfo("Message","Congratulations! You correctly completed the Sudoku puzzle")

def solve(arr):
    if validspot(arr) == False:
        return 'done'
    i = validspot(arr)[0]
    j = validspot(arr)[1]
    for x in range(1,10):
        time.sleep(.003)
        arr[i][j] = x
        storage[i][j].button["text"] = x
        if istrue(arr,i,j) == True:
            y = solve(arr)
            if y == 'done':
                return 'done'
            
    arr[i][j] = 0
    return False
solve_button = Button(root,text="Solve Using Backtracking", command = lambda: solve(arr))
solve_button.place(x = 400, y = 600, width = 300, height = 20)
check_button = Button(root,text='Check',command = lambda: check_board(arr))
check_button.place(x = 50, y = 600, width = 300, height = 20)
root.mainloop()