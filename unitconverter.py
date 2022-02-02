# A unit Converter App - From Inch to CM
# Import tkinter Module

from tkinter import *

# Create a function


def convert():
    if inch_data.get() != "":
        cm_string = str(int(inch_data.get()) * 2.54)
        cm_display.configure(text=cm_string)


window = Tk()
window.title("Inch to Cm Converter")

inch_data = Entry(window, text="")
inch_data.pack()

cm_display = Label(window, text="")
cm_display.pack()

button = Button(window, text="convert to CM", command=convert)
button.pack()

window.mainloop()
