# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.title("simple") # window title
window.geometry("500x500") # width x height

button = Button(window, text="Click me", command=lambda: print("Button clicked"), width= 12)

button.place(x = 200, y= 200)


# step 4 : main loop

mainloop()