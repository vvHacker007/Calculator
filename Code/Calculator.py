# We are importing everything from the tkinter library
from tkinter import *

# With this we are making a window widget
window = Tk()

# Putting a title to the window
window.title("Calculator")

# Giving the Program an icon
# window.wm_iconbitmap("calculator_icon.ico")

# Now we create an entry widget
e = Entry(window, width=65, borderwidth=5, bg="black", fg="white")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)




"""
Creating a button widget
state=disabled would not alow us to click the button
padx and pady helps in resizing the button
fg for foreground colour
bg for back ground colour
"""
# Here we will define how the numbers should be inserted in the window
def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Defining the functions which would be used in the calculator
def clear():
    e.delete(0, END)


def add():
    f_num = e.get()
    global num2
    global math
    math = "add"
    num2 = float(f_num)
    e.delete(0, END)


def sub():
    f_num = e.get()
    global num2
    global math
    math = "sub"
    num2 = float(f_num)
    e.delete(0, END)


def mul():
    f_num = e.get()
    global num2
    global math
    math = "mul"
    num2 = float(f_num)
    e.delete(0, END)


def div():
    f_num = e.get()
    global num2
    global math
    math = "div"
    num2 = float(f_num)
    e.delete(0, END)


def per():
    f_num = e.get()
    global num2
    global math
    math = "per"
    num2 = float(f_num)
    e.delete(0, END)


def square():
    f_num = e.get()
    global num2
    global math
    math = "square"
    num2 = float(f_num)
    e.delete(0, END)


def inv():
    f_num = e.get()
    global num2
    global math
    math = "inv"
    num2 = float(f_num)
    e.delete(0, END)


def equal():

    s_num = e.get()
    e.delete(0, END)
    if(math == "add"):
        num3 = float(s_num) + float(num2)


    elif(math == "sub"):
        num3 = float(num2) - float(s_num)



    elif(math == "mul"):
        num3 = float(s_num) * float(num2)



    elif(math == "div"):
        num3 = float(num2) / float(s_num)



    elif(math == "per"):
        num3 = (float(s_num) / float(num2))/100



    elif(math == "square"):
        num3 = int(num2) * int(num2)



    elif(math == "inv"):
        num3 = 1/float(num2)

    e.insert(0, num3)


# Define buttons and putting on the screen
button_1 = Button(window, text="1", padx=40, pady=40, command=lambda: click(1), bg="black", fg="white").grid(row=1, column=0, columnspan=1, rowspan=1)
button_2 = Button(window, text="2", padx=40, pady=40, command=lambda: click(2), bg="black", fg="white").grid(row=1, column=1, columnspan=1, rowspan=1)
button_3 = Button(window, text="3", padx=40, pady=40, command=lambda: click(3), bg="black", fg="white").grid(row=1, column=2, columnspan=1, rowspan=1)
button_4 = Button(window, text="4", padx=40, pady=40, command=lambda: click(4), bg="black", fg="white").grid(row=2, column=0, columnspan=1, rowspan=1)
button_5 = Button(window, text="5", padx=40, pady=40, command=lambda: click(5), bg="black", fg="white").grid(row=2, column=1, columnspan=1, rowspan=1)
button_6 = Button(window, text="6", padx=40, pady=40, command=lambda: click(6), bg="black", fg="white").grid(row=2, column=2, columnspan=1, rowspan=1)
button_7 = Button(window, text="7", padx=40, pady=40, command=lambda: click(7), bg="black", fg="white").grid(row=3, column=0, columnspan=1, rowspan=1)
button_8 = Button(window, text="8", padx=40, pady=40, command=lambda: click(8), bg="black", fg="white").grid(row=3, column=1, columnspan=1, rowspan=1)
button_9 = Button(window, text="9", padx=40, pady=40, command=lambda: click(9), bg="black", fg="white").grid(row=3, column=2, columnspan=1, rowspan=1)
button_sqr = Button(window, text="sqr", padx=35, pady=40, command=square, bg="black", fg="white").grid(row=4, column=0, columnspan=1, rowspan=1)
button_0 = Button(window, text="0", padx=40, pady=40, command=lambda: click(0), bg="black", fg="white").grid(row=4, column=1, columnspan=1, rowspan=1)
button_inv = Button(window, text="inv", padx=35, pady=40, command=inv, bg="black", fg="white").grid(row=4, column=2, columnspan=1, rowspan=1)


button_add = Button(window, text=" + ", padx=49, pady=40, command=add, bg="black", fg="white").grid(row=1, column=3, columnspan=1, rowspan=1)
button_sub = Button(window, text="-", padx=40, pady=40, command=sub, bg="black", fg="white").grid(row=1, column=4, columnspan=1, rowspan=1)
button_mul = Button(window, text=" * ", padx=50, pady=40, command=mul, bg="black", fg="white").grid(row=2, column=3, columnspan=1, rowspan=1)
button_div = Button(window, text="/", padx=40, pady=40, command=div, bg="black", fg="white").grid(row=2, column=4, columnspan=1, rowspan=1)
button_equal = Button(window, text="=", padx=38, pady=92, command=equal, bg="blue", fg="white").grid(row=3, column=4, columnspan=1, rowspan=2)
button_clear = Button(window, text="Clear", padx=42, pady=40, command=clear, bg="black", fg="white").grid(row=3, column=3, columnspan=1, rowspan=1)
button_per = Button(window, text="% ", padx=49, pady=40, command=per, bg="black", fg="white").grid(row=4, column=3, columnspan=1, rowspan=1)


# With this the window will run in an infinite loop until it is not manually closed
window.mainloop()


