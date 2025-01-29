from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_x = Label(text="Timer",fg="Black", bg=YELLOW,font=(FONT_NAME,25,"bold"))
timer_x.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
canvas.create_text(100,120,text="00:00",font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(column=2,row=2)

checkmark = Label(text="✔", bg=YELLOW, highlightbackground=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)



window.mainloop()
