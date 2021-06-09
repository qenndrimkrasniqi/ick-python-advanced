import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

label1 = tk.Label(master=window, text='1', bg='black', fg='white')
label2 = tk.Label(master=window, text='2', bg='black', fg='white')
label3 = tk.Label(master=window, text='3', bg='black', fg='white')
label4 = tk.Label(master=window, text='4', bg='black', fg='white')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky='ew')
label3.grid(row=0, column=2, sticky='ns')
label4.grid(row=0, column=3, sticky='nsew')

window.mainloop()