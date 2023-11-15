#simple GUI with the help of Tkinter library to find out the data type of a value in Python programming.

from tkinter import *
import tkinter as tk

def check_datatype():
    input_value = value.get()
    try:
        out = type(eval(input_value))
        output.config(text=f'{input_value} is a {out}')

    except (SyntaxError, NameError):
        if type(input_value) == str:
            out = type(input_value)
            output.config(text=f'{input_value} is a {out}')
        else:
            out = 'Invalid option'
            output.config(text=f'{input_value} is a {out}')

root = tk.Tk()
root.geometry('500x300')
root.title('Data type finder')

Label(root, text='Hi, here you can find the data type of a value').pack(pady=10)
Label(root, text='Enter the value below:').pack(pady=5)

value = StringVar()
entry = Entry(root, textvariable=value).pack(pady=5)

Label(root, text='Select an option:').pack(pady=5)

Button(root, text='Check', command=check_datatype).pack(pady=10)

output = Label(root, text='')
output.pack(pady=10)

root.mainloop()
