#!/usr/bin/python3
'''
Docs go here!
'''
import tkinter as tk
from tkinter import ttk, N,W, E, S


OLD_VALUE = 0
NEW_VALUE = 0
OPERATION = '+'
LAST_BUTTON = '+'


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


def apply_operation(operation):
    global NEW_VALUE
    global OLD_VALUE
    global OPERATION
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

buttons = [
    ['1', '2', '3', '/'],
    ['4', '5', '6', 'x'],
    ['7', '8', '9', '-'],
    ['0', '.', '=', '+']
]

numbers = [str(i) for i in range(1, 10)] + ['0', '.']


operations = ['/', 'x', '-', '+', '=']

buttons = dict()
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



# text = tk.Text(mainframe, width=75, height = 20)
# text.grid(column=2, row=1, sticky=(W, E))
#
# filename_entry = ttk.Entry(mainframe, width = 5, textvariable = filename)
# filename_entry.grid(column = 2, row = 2)
#
# ttk.Label(mainframe).grid(column=1, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Save", command=save).grid(column=3, row=3, sticky=W)
# ttk.Checkbutton(mainframe, text='yay text!', onvalue = 'foo', offvalue = 'bar').grid(column = 3, row = 4)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()
