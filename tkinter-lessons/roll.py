import random
import tkinter as tk

window = tk.Tk()

def roll_dice():
    label['text'] = random.choice(range(1, 7))

button = tk.Button(
    master=window, text="Roll", height=2, width=15, command=roll_dice
)
button.pack()

label = tk.Label(master=window, text='1', height=2, width=15)
label.pack()

window.mainloop()