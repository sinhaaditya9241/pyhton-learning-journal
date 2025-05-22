# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.title("simpel drawing")

c = Canvas(window,width = 500, height = 500)
c.pack()
c.create_line(0,0 ,500,500, width=5, fill='blue')
c.create_rectangle(150, 125, 450, 375 , fill='red')

# step 4 : main loop

mainloop()