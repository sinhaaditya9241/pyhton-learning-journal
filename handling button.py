# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.title("simple") # window title
window.geometry("500x500") # width x height

def log_entry():
    print("logged in")



button = Button(window, text="LOGIN" , command=log_entry, bg="blue", fg="white",width= 12, font= ("Arial", 12), activebackground="black", activeforeground="white")
button.pack()



# step 4 : main loop

mainloop()