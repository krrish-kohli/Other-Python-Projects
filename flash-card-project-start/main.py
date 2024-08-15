from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=old_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=new_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Setting up the window.
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Adding the flash card.
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
old_img = PhotoImage(file="images/card_front.png")
new_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=old_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Adding wrong button.
my_image1 = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=my_image1, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(column=0, row=1)

# Adding right button.
my_image2 = PhotoImage(file="images/right.png")
known_button = Button(image=my_image2, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
