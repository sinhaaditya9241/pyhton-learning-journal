# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.geometry('500x500')
'''
massage = Message(window, text = "Enter your name", font = ('Arial', 20))
massage.pack()
'''
var = StringVar()
ent_var = StringVar()

def insert():
    result = ent_var.get()
    var.set(result)

massage = Message(window, textvariable= var , relief= RAISED, font = ('Arial', 20), padx= 50, pady= 50)
entry = Entry(window, textvariable = ent_var, font = ('Arial', 20))
button = Button(window, text= "ok " , command= insert)
massage.pack()
entry.pack()
button.pack()

# step 4 : main loop

mainloop()