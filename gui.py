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
#storage stores the buttons to access their text block.(list of cube objects).
storage = []
#The main class and the spaces on the sudoku board as buttons.
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
#creates the board with all the buttons and stores the buttons in storage for later use.
for i in range(0,9):
    storage.append([])
    for j in range(0,9):
        b = cube(arr,i,j)
        storage[i].append(b)
        b.button.place(y = i * 50, x = j * 80, width = 80, height = 50)
#function that runs after clicking the Check button to see if the board is correct or not.
def check_board(arr):
    for i in range(0,9):
        for j in range(0,9):
            if istrue(arr,i,j) == False:
                messagebox.showinfo('Message', 'Sorry but your answer is not correct! Try Again!')
                return False
    messagebox.showinfo("Message","Congratulations! You correctly completed the Sudoku puzzle")
#function that runs when clicking solve and uses the backtracking algorithm to solve the board and give the solution to the board.
def solve(arr):
    if validspot(arr) == False:
        return 'done'
    i = validspot(arr)[0]
    j = validspot(arr)[1]
    for x in range(1,10):
        time.sleep(.003)
        arr[i][j] = x
        storage[i][j].button["text"] = x
        root.update()
        if istrue(arr,i,j) == True:
            y = solve(arr)
            if y == 'done':
                return 'done'
            
    arr[i][j] = 0
    return False
#This function is the same as the solve function, but there is no update() so the visualization is skipped the answer is presented immediately
def solve2(arr, storage):
    if validspot(arr) == False:
        return 'done'
    i = validspot(arr)[0]
    j = validspot(arr)[1]
    for x in range(1,10):
        time.sleep(.003)
        arr[i][j] = x
        storage[i][j].button["text"] = x
        if istrue(arr,i,j) == True:
            y = solve2(arr,storage)
            if y == 'done':
                return 'done'
            
    arr[i][j] = 0
    return False
#This function runs when the reset button is clicked and resets the board to zeroes to be filled in once again.
def reset(arr,storage):
    for i in range(0,9):
        for j in range(0,9):
            arr[i][j] = 0
            storage[i][j].button["text"] = str(0)
#code to setup external buttons and the mainloop.
solve_button = Button(root,text="Solve Using Backtracking", command = lambda: solve(arr))
solve_button.place(x = 400, y = 600, width = 300, height = 20)
check_button = Button(root,text='Check',command = lambda: check_board(arr))
check_button.place(x = 50, y = 600, width = 300, height = 20)
reset_button = Button(root,text="Reset", command = lambda: reset(arr,storage))
reset_button.place(x = 400, y = 500 , width = 300, height = 20)
solve_button2 = Button(root, text="Solve(without Visualization)", command = lambda: solve2(arr,storage))
solve_button2.place(x = 50, y = 500, width = 300, height = 20)
root.mainloop()