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
tick = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    windows.after_cancel(timer)
    canvas.itemconfig(canvas_timer, text="00:00")
    head_label.config(text="Timer", fg=GREEN)
    global tick
    tick = ""
    tick_label.config(text=tick)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        head_label.config(text='Relax', fg=GREEN)
        count_down(long_break)
    elif reps % 2 == 0:
        head_label.config(text='Short Break', fg=PINK)
        count_down(short_break)
    else:
        head_label.config(text='Work Time', fg=RED)
        count_down(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global tick
            tick += '✔'
            tick_label.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Timer")
windows.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
picture = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=picture)
canvas_timer = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

head_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, 'normal'))
head_label.grid(column=1, row=0)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset)
reset_button.grid(column=2, row=2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

windows.mainloop()
