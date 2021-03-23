from tkinter import *


def circle():
    """
    Calculate area and circumreference, then return answer.
    """
    pi = 3.1415  # I don't want to import math
    if str(radius.get()).isdigit():
        if radius.get() >= 0:
            area = Label(window, text=f"Area:{round((pi * float(radius.get()) ** 2), 2)}\n"
                                      f"Circumreference:{round(pi * float(radius.get()) * 2, 2)}", justify=LEFT)
            area.grid(column=0, row=1)  # position of answer text


window = Tk()
window.title("errodi area and circumreference calculator")  # Create title of window
window.geometry("400x75")  # define size of window
label = Label(window, text="Please enter radius of circle")
label.grid(column=0, row=0)  # position of text
radius = Entry(window, width=10)  # create dialog box
radius.insert(0, "here")
radius.grid(column=1, row=0)  # position of dialog box
btn = Button(window, text="calculate!", command=circle).grid(column=2, row=0)  # create calculate! button
area = Label(window, text="Area:\nCircumreference:", justify=LEFT).grid(column=0, row=1)
window.mainloop()
