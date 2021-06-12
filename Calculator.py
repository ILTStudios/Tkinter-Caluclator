import tkinter
from tkinter import *

#Creating GUI Window
GUI = tkinter.Tk()
GUI.configure(background = "light green")
GUI.title("Calculator")
GUI.geometry("800x600")

def press(num):
    TextField.insert(100, num)
def Button_Clear():
    TextField.delete(0,100)
def Equate():
    Expression = TextField.get()
    TextField.delete(0,100)
    Result = eval(Expression)
    print(Result)
    TextField.insert(0, str(Result))

#Creating Buttons In GUI Window
TextField = Entry(GUI, width = 20)
TextField.grid(columnspan = 4, ipadx = 70)

Button1 = Button(GUI, text = "1", fg = "Black", bg = "white", command = lambda:press(1), height = 1, width = 7) 
Button1.grid(row = 2, column = 0)

Button2 = Button(GUI, text = "2", fg = "Black", bg = "White", command = lambda:press(2), height = 1, width = 7)
Button2.grid(row = 2, column = 1)

Button3 = Button(GUI, text = "3", fg = "Black", bg = "White", command = lambda:press(3), height = 1, width = 7)
Button3.grid(row = 2, column = 2)

Button4 = Button(GUI, text = "4", fg = "Black", bg = "White", command = lambda:press(4), height = 1, width = 7)
Button4.grid(row = 3, column = 0)

Button5 = Button(GUI, text = "5", fg = "Black", bg = "White", command = lambda:press(5), height = 1, width = 7)
Button5.grid(row = 3, column = 1)

Button6 = Button(GUI, text = "6", fg = "Black", bg = "White", command = lambda:press(6), height = 1, width = 7)
Button6.grid(row = 3, column = 2)

Button7 = Button(GUI, text = "7", fg = "Black", bg = "White", command = lambda:press(7), height = 1, width = 7)
Button7.grid(row = 4, column = 0)

Button8 = Button(GUI, text = "8", fg = "Black", bg = "White", command = lambda:press(8), height = 1, width = 7)
Button8.grid(row = 4, column = 1)

Button9 = Button(GUI, text = "9", fg = "Black", bg = "White", command = lambda:press(9), height = 1, width = 7)
Button9.grid(row = 4, column = 2)

Button0 = Button(GUI, text = "0", fg = "Black", bg = "white", command = lambda:press(0), height = 1, width = 7)
Button0.grid(row = 5, column = 0)

ButtonPlus = Button(GUI, text = "+", fg = "Black", bg = "White", command = lambda:press("+"), height = 1, width = 7)
ButtonPlus.grid(row = 2, column = 3)

ButtonMinus =  Button(GUI, text = "-", fg = "Black", bg = "White", command = lambda:press("-"), height = 1, width = 7)
ButtonMinus.grid(row = 3, column = 3)

ButtonMultiply =  Button(GUI, text = "*", fg = "Black", bg = "White", command = lambda:press("*"), height = 1, width = 7)
ButtonMultiply.grid(row = 4, column = 3)

ButtonDivide =  Button(GUI, text = "/", fg = "Black", bg = "White", command = lambda:press("/"), height = 1, width = 7)
ButtonDivide.grid(row = 5, column = 3)

ButtonEqual = Button(GUI, text = "=", fg = "Black", bg = "White", command = Equate, height = 1, width = 7)
ButtonEqual.grid(row = 5, column = 2)

ButtonClear = Button(GUI, text = "Clear", fg = "Black", bg = "White", command = Button_Clear, height = 1, width = 7)
ButtonClear.grid(row = 5, column = 1)

ButtonDecimal = Button(GUI, text = ".", fg = "Black", bg = "White", command = lambda:press("."), height = 1, width = 7)
ButtonDecimal.grid(row = 6, column = 0)

GUI.mainloop()