import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):

        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=10, pady=10)

        label = tk.Label(master=frame, text=f'Row: {i}, Column: {j}')
        label.pack(padx=10, pady=10)

"""
frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame1.grid(row=0, column=1)

label1 = tk.Label(master=frame1, text='Row: 0, Column: 1')
label1.pack()

frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame2.grid(row=1, column=2)

label2 = tk.Label(master=frame2, text='Row: 1, Column: 2')
label2.pack()
"""

window.mainloop()
