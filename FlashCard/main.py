from tkinter import *
import pandas as pd
import random as rnd

# DataFrame'i küresel olarak tanımla
data_set = pd.read_csv("Dateset.csv")
data_dict = data_set.to_dict()
data_dict_english = data_dict["Engilish"]
data_dict_turkish = data_dict["Türkçe"]

window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg="#B1DDC6")

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg="#B1DDC6", highlightthickness=0)

text_languge = canvas.create_text(400, 158, text="Engilish", fill="black", font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

# Başlangıçta rastgele bir indeks seç
current_index = None

def go_next_word():
    # Global değişkeni kullan
    global current_index
    current_index = rnd.randint(0, 2000)

def show_english():
    go_next_word()  # Her butona basıldığında yeni bir indeks seç
    new_en_value = data_dict_english[current_index]
    canvas.itemconfigure(text_word, text=new_en_value)
    canvas.itemconfigure(text_languge,text="Engilish")
    window.after(3000, show_turkish)

def show_turkish():
    new_tr_value = data_dict_turkish[current_index]
    canvas.itemconfigure(text_word, text=new_tr_value)
    canvas.itemconfigure(text_languge,text="Türkçe")

right_button_img = PhotoImage(file="right.png")
right_button = Button(window, image=right_button_img, highlightthickness=0, command=show_english)
right_button.grid(column=0, row=1)

wrong_button_img = PhotoImage(file="wrong.png")
wrong_button = Button(window, image=wrong_button_img, highlightthickness=0, command=show_english)
wrong_button.grid(column=1, row=1)

# PhotoImage nesnelerini referans olarak sakla
right_button.image = right_button_img
wrong_button.image = wrong_button_img

window.mainloop()
