# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.title("simple") # window title
window.geometry("500x700") # width x height
window.config(bg= "yellow") # background color

frame1 = Frame(window, bg="red",width=300 , height=303 , cursor="dot") # frame 1
frame2 = Frame(window , bg = "green" , width = 300, height = 300, cursor= "dotbox") # frame 2

Button1 = Button(frame1, text = "button1", bg = "blue")
button2 = Button(frame2, text = "button2", bg = "pink")
button3 = Button(frame1 , text = "logged", fg = "red")

frame1.pack(side= TOP) # frame 1 position
frame2.pack(side = BOTTOM) # frame 2 position
Button1.pack()
button2.pack()
button3.pack()


# step 4 : main loop

mainloop()