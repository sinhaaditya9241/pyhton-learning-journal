# step 1 : importing
from tkinter import *



# step 2 : gui interaction
window = Tk()
window.geometry('500x500')
window.title("aditya's calculator")
window.config(bg = "yellow")


# step 3 : adding inputs 

# menu box
menu = Menu(window)
file = Menu(menu, tearoff=0)
file.add_command(label="exit", command=lambda:
                  window.destroy())

# ENTRY BOX
entry_box = Entry(window, width=56, borderwidth=5)
entry_box.place(x = 0 , y = 0 )

# BUTTONS
def click(num):
    result = entry_box.get()
    entry_box.insert(0 , str(result) + str(num))

button_1 = Button(window, text = "1", width= 12, command= lambda:
                  click(1))
button_1.place(x = 10, y = 60 )

button_2 = Button(window, text = "2", width= 12, command= lambda:
                  click(2))
button_2.place(x = 80 , y = 60 )

button_3 = Button(window, text = "3", width= 12, command= lambda:
                  click(3))
button_3.place(x = 170 , y = 60 )

button_4 = Button(window, text = "4", width= 12, command= lambda:
                  click(4))
button_4.place(x = 10 , y = 120 )

button_5 = Button(window, text = "5", width= 12, command= lambda:
                  click(5))
button_5.place(x = 80 , y = 120 )

button_6 = Button(window, text = "6", width= 12, command= lambda:
                  click(6))
button_6.place(x = 170 , y = 120 )

button_7 = Button(window, text = "7", width= 12, command= lambda:
                  click(7))          
button_7.place(x = 10 , y = 180 )

button_8 = Button(window, text = "8", width= 12, command= lambda:
                  click(8))
button_8.place(x = 80 , y = 180 )

button_9 = Button(window, text = "9", width= 12, command= lambda:
                  click(9))
button_9.place(x = 170 , y = 180 )

button_0 = Button(window, text = "0", width= 12, command= lambda:
                  click(0))
button_0.place(x = 10 , y = 240 )

# operator
def add():
    n1 = entry_box.get()
    global math
    global i
    math = "add"
    i = int(n1)
    entry_box.delete(0, END)

button_a = Button(window, text = "+", width= 12, command= add)
button_a.place(x = 80 , y = 240 )

def sub():
    n1 = entry_box.get()
    global math
    global i
    math = "subtract"
    i = int(n1)
    entry_box.delete(0, END)

button_s = Button(window, text = "-", width= 12, command= sub)
button_s.place(x = 170 , y = 240 )

def mut():
    n1 = entry_box.get()
    global math
    global i
    math = "multiplication"
    i = int(n1)
    entry_box.delete(0, END)

button_m = Button(window, text = "*", width= 12, command= mut)
button_m.place(x = 10 , y = 300 )

def div():
    n1 = entry_box.get()
    global math
    global i
    math = "division"
    i = int(n1)
    entry_box.delete(0, END)

button_d = Button(window, text = "/", width= 12, command= div)
button_d.place(x = 80 , y = 300 )

def equal():
    n2 = entry_box.get()
    global i
    result = i + int(n2)
    entry_box.delete(0, END)
    if math == "add":
        entry_box.insert(0, i + int(n2))
    elif math == "subtract":
        entry_box.insert(0, i - int(n2))
    elif math == "multiplication":
        entry_box.insert(0, i * int(n2))
    elif math == "division":
        entry_box.insert(0, i / int(n2))
    

button_e = Button(window, text = "=", width= 12, command= equal)
button_e.place(x = 170 , y = 300 )

def clear():
    entry_box.delete(0, END)


button_c = Button(window, text = "clear", width= 12, command= clear)
button_c.place(x = 10 , y = 350 )


# step 4 : mainloop

mainloop()