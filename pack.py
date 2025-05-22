# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.title("simple") # window title
window.geometry("500x500") # width x height
window.config(bg= "yellow") # background color

label1 = Label(window, text="Enter your name", bg="blue")
label1.pack(side= TOP, fill=X, expand= False)
label2 = Label(window, text="Enter your age", bg="red")
label2.pack(side= LEFT, fill=Y, expand= False)
lable3 = Label(window, text="Enter your email", bg="green")
lable3.pack(side= RIGHT, fill=Y, expand= False)
lable4 = Label(window, text="Enter your phone", bg="purple")
lable4.pack(side= BOTTOM, fill=X, expand= False)




# step 4 : main loop

mainloop()