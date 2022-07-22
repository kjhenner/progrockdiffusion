from tkinter import *
import json

json_set = json.load(open('settings.json'))

window = Tk()

master_frame = Frame(bg='Light Blue', bd=3, relief=RIDGE)
master_frame.grid(sticky=NSEW)
master_frame.columnconfigure(0, weight=1)


r = 0
c = 0

for key, value in json_set.items():
    text = StringVar()
    text.set(value)
    Label(window, text=key).grid(row=r, column=c)
    r = r + 1
    textBox = Entry(window, textvariable=text).grid(row=r, column=c)
    r = r + 1

r = 0
c = 0

window.mainloop()
