from tkinter import *

# 1. gui interation
window = Tk()
window.geometry("500x500")

# 2. Adding inputs
a = Entry(window, width=50, borderwidth=10)
a.place(x=0, y=0)

#BUTTONS
def click(number):
    result = a.get()
    a.delete(0, END)
    a.insert(0, str(result) + str(number))

b = Button(window, text ='1', width=12, height=2, command=lambda:click(1))
b.place(x=10, y=60)

b = Button(window, text ='2', width=12, height=2, command=lambda:click(2))
b.place(x=110, y=60)

b = Button(window, text ='3', width=12, height=2, command=lambda:click(3))
b.place(x=210, y=60)

b = Button(window, text='4', width=12, height=2, command=lambda:click(4))
b.place(x=10, y=120)

b = Button(window, text ='5', width=12, height=2, command=lambda:click(5))
b.place(x=110, y=120)

b = Button(window, text ='6', width=12, height=2, command=lambda:click(6))
b.place(x=210, y=120)

b = Button(window, text ='7', width=12, height=2, command=lambda:click(7))
b.place(x=10, y=180)

b = Button(window, text ='8', width=12, height=2, command=lambda:click(8))
b.place(x=110, y=180)

b = Button(window, text ='9', width=12, height=2, command=lambda:click(9))
b.place(x=210, y=180)

b = Button(window, text ='0', width=12, height=2, command=lambda:click(0))
b.place(x=10, y=240)


#Operators
def add():
    n1 = a.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    a.delete(0, END)

b = Button(window, text ='+', width=12, height=2, command=add)
b.place(x=110, y=240)

def subtract():
    n1 = a.get()
    global math
    math = 'subtraction'
    global i
    i = int(n1)
    a.delete(0, END)

b = Button(window, text ='-', width=12, height=2, command=subtract)
b.place(x=210, y=240)

def multiply():
    n1 = a.get()
    global math
    math = 'multiplication'
    global i
    i = int(n1)
    a.delete(0, END)

b = Button(window, text ='*', width=12, height=2, command=multiply)
b.place(x=10, y=300)


def divide():
    n1 = a.get()
    global math
    math = 'division'
    global i
    i = int(n1)
    a.delete(0, END)

b = Button(window, text ='/', width=12, height=2, command=divide)
b.place(x=110, y=300)

def equal():
    n2 = a.get()
    a.delete(0, END)
    if math == 'addition':
        result = i + int(n2)
        a.insert(0, result)
    elif math == 'subtraction':
        result = i - int(n2)
        a.insert(0, result)
    elif math == 'multiplication':
        result = i * int(n2)
        a.insert(0, result)
    elif math == 'division':
        result = i / int(n2)
        a.insert(0, result)


b = Button(window, text ='=', width=12, height=2, command=equal)
b.place(x=210, y=300)


def clear():
    a.delete(0, END)

b = Button(window, text ='clear', width=12, height=2, command=clear)
b.place(x=110, y=350)

mainloop()