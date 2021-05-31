import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame(master=window)
frame_b = tk.Frame(master=window)


label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_b.pack()
frame_a.pack()

window.mainloop()
