""""
Flash Card App - Learning Made Fun
Version 0: Supports French
Version 1: Supports any .csv file that contains langauge and its English Translation
"""
import random
from tkinter import *
from tkinter import messagebox, simpledialog
import pandas as pd
import new_mod

BACKGROUND_COLOR = "#B1DDC6"

# --------------Creating Flash Cards---------------#
# TODO : Using New MOD to parser the available language csv files
language_list = new_mod.language_parser()
# print(my_language_list)
# Deprecated language list
# # language_list = ["French"]
current_card = {}
global language
to_learn = {}

def play():
    global language,flip_timer,to_learn
    language = simpledialog.askstring(title="Select Language", prompt="Which language to learn?").title()
    if language in language_list:
        # TODO : Read the language
        try:
            data = pd.read_csv(f'./Data/{language.lower()}_tolearn.csv')
        except FileNotFoundError:
            original_data = pd.read_csv(f'./Data/{language.lower()}_words.csv')
            to_learn = original_data.to_dict(orient="records")
        else:
            # Converting data into dictionary; Orient as record gives me a list of key-value dict.
            to_learn = data.to_dict(orient="records")

        # TODO :  Start Flipping card sequence for the first card
        flip_timer = window.after(3000, flip_card)
        new_card()
    # TODO :  Disable play button once language is set.
        play_button["state"]="disabled"
    else:
        messagebox.showwarning(title="Oops 🤭", message="Currently this language is not supported !")


def new_card():
    global current_card, flip_timer
    # Invalidating flip timer for new card for successful multiple clicks.
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(canvas_lang, text=language, fill="black")
    canvas.itemconfig(canvas_word, text=current_card[language], fill="black")
    canvas.itemconfig(front, image=front_image)
    window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(f"./Data/{language.lower()}_tolearn.csv",index=False)
    new_card()


def flip_card():
    canvas.itemconfig(front, image=back_image)
    canvas.itemconfig(canvas_lang, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")


# --------------UI SETUP---------------#
window = Tk()
window.title('Fash Cards')
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
# Flip the card first time
# flip_timer = window.after(5000, flip_card)
global flip_timer
# TODO : Place Image and Make Canvas Ready
canvas = Canvas(width=800, height=526, highlightthickness=0)

front_image = PhotoImage(file='./Image/card_front.png')
back_image = PhotoImage(file='./Image/card_back.png')
front = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas_lang = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=3)

# TODO : Place Buttons
cross_image = PhotoImage(file="Image/wrong.png")
tick_image = PhotoImage(file="Image/right.png")
play_image = PhotoImage(file="Image/play.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=new_card)
tick_button = Button(image=tick_image, highlightthickness=0, command=is_known)
play_button = Button(image=play_image, highlightthickness=0, command=play)
cross_button.grid(row=1, column=0)
play_button.grid(row=1, column=1)
tick_button.grid(row=1, column=2)

window.mainloop()
