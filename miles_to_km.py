from logging import makeLogRecord
from tkinter import *
window = Tk()
window.title("Miles to Km converter")
window.minsize(width=150,height=150)
window.config(padx=15, pady=15)

#button
def clicked_on():
    print(input.get())
    new = int(input.get()) * 1.6
    new = int(new)
    converted_value.config(text=f"{new}")


button = Button(text="Convert",command=clicked_on)
button.grid(column=1, row=2)

input = Entry(width=5)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

blank = Label(text="         ")
blank.grid(column=0, row=0)

is_equal = Label(text="Is equal to ")
is_equal.grid(column=0, row=1)

converted_value = Label(text=0)
converted_value.grid(column=1, row=1)

window.mainloop()

