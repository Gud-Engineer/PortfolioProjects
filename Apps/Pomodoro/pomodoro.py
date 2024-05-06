""""
The POMODORO Technique is an acclaimed Time-Management System
that has transformed.
POMODORO re-wires the brain to take short breaks and improve information retention !!
The technique can be broken down as :
    Essentially one figures out the task that needs to be done,
    Sets the timer for 25 mins and works on it until timer rings,
    Takes a short break of 5 mins.
    Do this 4 times before taking a big break of 15-30 mins.
---------------------------------
The program is a timer with two buttons : START and RESET
clicking start-> sets it for 4 : 25min-5min cycles before longer break or reset button is clicked
Places check marks for each cycle and Pops Up when Break is scheduled.
"""
from tkinter import *

# -------------CONSTANTS---------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1 #25
SHORT_BREAK_MIN = 0.1 #5
LONG_BREAK_MIN =  0.1 #20
reps = 0
tic = NONE

# --------------TIMER RESET---------------#
def reset_timer():
    # TODO : Stop Timer
    window.after_cancel(tic)
    # TODO : Default to Starting Screen
    timer_label.config(text="Timer")
    tick_label.config(text="Progress : ")
    canvas.itemconfig(canvas_img,image=start_img)
    canvas.itemconfig(timer_text,text=" 00 : 00 ")
    global reps
    reps = 0


# --------------TIMER MECHANISM----------#
def start_timer():
    global reps
    reps += 1
    # TODO : 25-5-25-5-25-5-25-20
    if reps == 8:
        canvas.itemconfig(canvas_img,image=relax_img)
        timer_label.config(text="LONG\nBREAK",fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        tick_label.config(text=f"✅✅✅✅",fg=GREEN)
        reps = 0  # Resetting rep, adding 1 tick

    elif reps%2 !=0:
        canvas.itemconfig(canvas_img, image=work_img)
        timer_label.config(text="WORK",fg=GREEN)
        count_down(WORK_MIN *60)
    else:
        canvas.itemconfig(canvas_img, image=relax_img)
        timer_label.config(text="BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        mark = " "
        work_sessions = reps//2
        for _ in range(work_sessions):
            mark+= "✅"
        tick_label.config(text=f"{mark}")

        print(f'Executing rep: {reps}')
    # count_down(5 * 60)  # Converting into sec


# --------------COUNTDOWN MECHANISM---------------#
def count_down(count):
    global tic
    count_min = count // 60
    count_sec = count % 60
    # ToDo : Time Formatting
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        tic = window.after(1000, count_down, count - 1)
    else:
        start_timer() # Starting timer for another activity set.

# --------------UI SETUP---------------#
window = Tk()
window.title("Pomodoro App ⚒️")
window.config(padx=50, pady=50, bg=YELLOW)
# TODO : Place Image
canvas = Canvas(width=230, height=230, bg=YELLOW, highlightthickness=0)
start_img = PhotoImage(file='tomato_start.png')
work_img = PhotoImage(file='tomato_working.png')
relax_img = PhotoImage(file='tomato_relaxing.png')
canvas_img = canvas.create_image(116, 116, image=start_img)
# canvas.create_image(116, 116, image=relax_img)
timer_text = canvas.create_text(130, 25, text=" 00 : 00 ", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# TODO : Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
tick_label = Label(text="Progress : ", fg=RED, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
timer_label.grid(row=0, column=1)
tick_label.grid(row=2, column=1)

# TODO : Buttons
start_button = Button(text="Start", font=("Times Now Roman", 12), command=start_timer)
reset_button = Button(text="Reset", font=("Times Now Roman", 12),command=reset_timer)
start_button.grid(row=3, column=0)
reset_button.grid(row=3, column=2)

window.mainloop()
