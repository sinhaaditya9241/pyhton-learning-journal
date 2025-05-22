# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
'''
window.title("simple") # window title
window.geometry("500x700") # width x height
'''
menu = Menu(window)
file = Menu(menu, tearoff=0)
file.add_command(label="New", command=lambda:
                 print("New file"))
file.add_command(label="Open", command=lambda:
                 print("Open file"))
file.add_separator() # add a separator
file.add_command(label="Save", command=lambda:
                 print("Save file"))
file.add_separator() # add a separator
file.add_command(label="Close", command=lambda: 
                 print("Close file")) 
file.add_command(label="Exit", command=lambda:
                 window.destroy())

menu.add_cascade(label="File", menu=file)
window.config(menu=menu)

# step 4 : main loop

mainloop()