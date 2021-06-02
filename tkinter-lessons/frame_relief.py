import tkinter as tk

window = tk.Tk()

"""
frame_a = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5)
frame_a.pack(side=tk.LEFT)
label_a = tk.Label(master=frame_a, text='flat')
label_a.pack()

frame_b = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame_b.pack(side=tk.LEFT)
label_b = tk.Label(master=frame_b, text='sunken')
label_b.pack()

frame_c = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frame_c.pack(side=tk.LEFT)
label_c = tk.Label(master=frame_c, text='raised')
label_c.pack()
"""

border_effect = {
    'flat': tk.FLAT,
    'sunken': tk.SUNKEN,
    'raised': tk.RAISED,
    'groove': tk.GROOVE,
    'ridge': tk.RIDGE
}

for relief_name, relief in border_effect.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()