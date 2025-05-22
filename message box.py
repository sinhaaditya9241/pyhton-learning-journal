# STEP 1 : import tkinter
from tkinter import *
import tkinter.messagebox


# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
tkinter.messagebox.showwarning("info", "hello world" )
question =  tkinter.messagebox.askyesno("option ", "do you want to continue?")

if question == True:
    print("yes")

else:
    print("no")


# step 4 : main loop

mainloop()