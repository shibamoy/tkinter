from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_x.config(text="Timer", fg="Black")
    global mark, reps
    mark = ""
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():

    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_x.config(text="Long Break", fg=PINK)
    elif reps % 2 ==0:
        countdown(SHORT_BREAK_MIN* 60)
        timer_x.config(text="Short Break", fg=PINK)
    else:
        countdown(WORK_MIN* 60)
        timer_x.config(text="GRINDD", fg=PINK)

        global mark
        mark += "✔"
        checkmark.config(text=mark)


def countdown(time_left):

    count_min = math.floor(time_left / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_seconds = time_left % 60
    if count_seconds == 0 or count_seconds <10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if time_left > 0:
        global timer
        timer = window.after(1000,countdown, time_left - 1)
    else:
        timer_start()


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
timer_text = canvas.create_text(100,120,text="00:00",font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command= timer_start)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2,row=2)

checkmark = Label(text="", bg=YELLOW, highlightbackground=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)



window.mainloop()
