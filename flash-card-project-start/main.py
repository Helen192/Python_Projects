from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

# current_word dictionary is used to save the current card. It is a global variable, so that we can take the translation of that word in both english and german
current_word = {}
to_learn = {}

try:
    dataset = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/German_English.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = dataset.to_dict(orient="records")


# function next_card, when user clicks on the known_button, a new random german word will appear.
# when user clicks on the unknown_button, a translation of that word in english will appear
def next_card():
    global current_word, flip_timer, words_to_learn
    window.after_cancel(flip_timer)
    # word is a random dictionary in the data_list
    current_word = random.choice(to_learn)
    canvas.itemconfig(title_text, text="German", fill="pink")
    canvas.itemconfig(word_text, text=current_word['German'], fill="pink")
    canvas.itemconfig(canvas_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

# flip the current card in german to english
def flip_card():
    canvas.itemconfig(title_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=current_word['English'], fill='white')
    canvas.itemconfig(canvas_background, image=back_img)

# when user click on the known_button, the current word is removed out of the list of words that user should learn
def is_known():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#_____________________________________ GUI design ______________________________________
# Create window
window = Tk()
window.title("Flash Card German - English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# After 3000ms canvas will be changed to green-background, and word in English
flip_timer = window.after(3000, func=flip_card)

# Create canvas with title and word front of background
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")
canvas_background = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"), fill="pink")
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="pink")

# Create Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
