import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    print(event.char)

def handle_click(event):
    print('The button was clicked!')

def handle_button_2(event):
    print('Button 2 was clicked')

def handle_button_3(event):
    print('Button 3 was clicked')

button = tk.Button(master=window, text='Click me!')
button.bind("<Button-1>", handle_click)
button.bind("<Button-2>", handle_button_2)
button.bind("<Button-3>", handle_button_3)
button.pack()

window.bind("<Key>", handle_keypress)


window.mainloop()
