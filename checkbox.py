# STEP 1 : import tkinter
from tkinter import *

# Step 2 : gui interaction

window = Tk()

# step 3 : adding inputs
window.title("simple") # window title
window.geometry("500x500") # width x height

Check_box_1 = IntVar()
Check_box_2 = IntVar()
Check_box_3 = IntVar()

chk_btn_1 = Checkbutton(window, text="check box 1", variable=Check_box_1)
chk_btn_2 = Checkbutton(window, text="check box 2", variable=Check_box_2)
chk_btn_3 = Checkbutton(window, text="check box 3", variable=Check_box_3)

chk_btn_1.pack()
chk_btn_2.pack()
chk_btn_3.pack()


# step 4 : main loop

mainloop()