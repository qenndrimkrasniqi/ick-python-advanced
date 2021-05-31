import tkinter as tk

window = tk.Tk()

greeting = tk.Label(
    master=window,
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10,
)

entry = tk.Entry(
    master=window,
    fg='yellow',
    bg='blue',
    width=50
)

greeting.pack()
entry.pack()

window.mainloop()
