# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.title("simple") # window title
window.geometry("250x50") # width x height
window.config(bg= "yellow") # background color
label1 = Label(window, text="mail", bg="blue") # label
label2 = Label(window, text="password", bg="blue") # label
button1 = Button(window, text="login") # button

e1 = Entry(window, width= 40, borderwidth=5)
e2 = Entry(window, width= 40, borderwidth=5)


label1.grid(row= 0 , column= 1) # grid position
label2.grid(row=1 , column= 1) # grid position
e1.grid(row= 0 , column= 2) # grid position
e2.grid(row= 1 , column= 2) # grid position
button1.grid(row=3, column= 2) # grid position

# step 4 : main loop

mainloop()