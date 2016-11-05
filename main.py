#!/usr/bin/python3
'''
Docs go here!
'''
import tkinter as tk
from tkinter import ttk, N,W, E, S

#Global variables that the calculator must hold in memory
OLD_VALUE = 0
NEW_VALUE = 0
OPERATION = '+'
LAST_BUTTON = '+'

#A helper function whenever a button is pressed
#routes 'number' and 'operation' buttons to their respective callback functions
def route_button(value, type_):
    global NEW_VALUE
    global OLD_VALUE
    global OPERATION
    global LAST_BUTTON
    if type_ == 'number':
        press_number(value)
    if type_ == 'operation':
        apply_operation(value)
    print(NEW_VALUE, OLD_VALUE, OPERATION)
    LAST_BUTTON = value

#the callback function when a number button is pressed
def press_number(number):
    global NEW_VALUE
    global OLD_VALUE
    global OPERATION
    global LAST_BUTTON
    if LAST_BUTTON in operations:
        disp = str(number)
    else:
        disp = DISPLAY_VALUE.get() + number
    if '.' not in disp:
        NEW_VALUE = int(disp)
        disp = str(NEW_VALUE)
    else:
        if number == '.':
            try:
                NEW_VALUE = float(disp)
            except ValueError:
                print ("User attempted decimal at incorrect time")
                disp = DISPLAY_VALUE.get()
        else:
            NEW_VALUE = float(disp)
            disp = str(NEW_VALUE)
    DISPLAY_VALUE.set(disp)

#the callback function when an operation button is pressed
def apply_operation(operation):
    global NEW_VALUE
    global OLD_VALUE
    global OPERATION
    global DISPLAY_VALUE
    temp = NEW_VALUE
    if OPERATION == '+':
        NEW_VALUE += OLD_VALUE
    elif OPERATION == '-':
        NEW_VALUE = OLD_VALUE - NEW_VALUE
    elif OPERATION == 'x':
        NEW_VALUE *= OLD_VALUE
    elif OPERATION == '/':
        NEW_VALUE = OLD_VALUE/NEW_VALUE
    elif OPERATION == '=':
        NEW_VALUE += 0 #do nothing
    OLD_VALUE = NEW_VALUE
    OPERATION = operation
    DISPLAY_VALUE.set(NEW_VALUE)

#the callback function when the clear button is pressed
def clear():
    global NEW_VALUE
    global OLD_VALUE
    global DISPLAY_VALUE
    global OPERATION
    if NEW_VALUE == 0:
        OLD_VALUE = 0
        OPERATION = '+'
    NEW_VALUE = 0
    DISPLAY_VALUE.set(NEW_VALUE)


root = tk.Tk()
root.title("Mafs")
root.resizable(0,0)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe['borderwidth'] = 10
mainframe['relief'] = 'sunken'

displayframe = ttk.Frame(mainframe, height = 30, width =150)
displayframe.grid(column=0, row=0)
displayframe['borderwidth'] = 5
displayframe['relief'] = 'sunken'

DISPLAY_VALUE = tk.StringVar()
DISPLAY_VALUE.set('0')


display = tk.Label(displayframe, textvariable = DISPLAY_VALUE, width = 15)
display.grid(column = 0, row = 0)


buttonframe = tk.Frame(mainframe)
buttonframe.grid(column=0, row=1)

#the list of numbers 0-9 plus the decimal in the order they'll
#appear on the calculator
numbers = [str(i) for i in range(1, 10)] + ['0', '.']

#the mathematical operations the calculator can perform
operations = ['/', 'x', '-', '+', '=']

#buttons is a dictionary containing all the buttons
#I'm building it in a dictionary via looping over the numbers buttons
#and operations buttons. I'm looping because adding each button explicitly
#is too redundant and there's a lot of overlap
buttons = dict()

#Add the numbers buttons first
row = 0
col = 0
for number in numbers:
    buttons[number] = {
        'row': row,
        'col': col,
        'value': number,
        'type': 'number'
        }
    col += 1
    if col == 3:
        col = 0
        row += 1

#now add the operations buttons
row = 0
col = 3
for operation in operations:
    if operation == '=':
        col = 2
        row = 3
    buttons[operation] = {
        'row': row,
        'col': col,
        'value': operation,
        'type': 'operation'
    }
    row += 1

#for each entry in the button dict, create a Button object that goes in
#the buttonframe. Give appropriate label, location, and callback function
for key in buttons:
    button = buttons[key]
    row = button['row']
    col = button['col']
    value = button['value']
    type_ = button['type']
    print(value, type_)
    button['button'] = tk.Button(buttonframe,
        text = value,
        command = lambda key=key: route_button(buttons[key]['value'], buttons[key]['type']))
    button['button'].grid(column = col, row = row, sticky = (N, S, E, W))

#add a "clear" button
tk.Button(buttonframe, text = 'C', command = clear).grid(column = 0, row = 4, sticky = (N, S, E, W), columnspan = 4)

#Give a little padding to each child
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()
