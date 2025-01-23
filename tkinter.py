from logging import makeLogRecord
from tkinter import *
window = Tk()
window.title("Gui project")
window.minsize(width=500,height=300)

#label
my_label = Label(text= "Label here", font=("Arial",24, "bold"))
my_label.pack()

my_label["text"] = "Newww"
my_label.config(text="hi")

#button
def clicked_on():
    print("clicked!")
    new = input.get()
    my_label.config(text=f"{new}")


button = Button(text="click me",command=clicked_on)
button.pack()

input = Entry(width=10)
input.pack()



window.mainloop()
