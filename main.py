from tkinter import *


def calculate_area(circle_radius: float):
    return round((3.1415 * circle_radius ** 2), 2)


def calculate_circumreference(circle_radius: float):
    return round(3.1415 * circle_radius * 2, 2)


def circle():
    """
    Calculate area and circumreference, then return answer.
    """
    pi = 3.1415  # I don't want to import math
    if str(radius.get()).isdigit():
        if radius.get() >= 0:
            area = Label(window, text=f"Area:{calculate_area(float(radius.get()))}\n"
                                      f"Circumreference:{calculate_circumreference(float(radius.get()))}", justify=LEFT)
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
