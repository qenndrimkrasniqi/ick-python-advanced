import tkinter as tk

window = tk.Tk()

entry = tk.Entry(master=window, fg='black', bg='white', width=40)
entry.pack()
entry.insert(tk.END, 'What is your name?')

entry1 = tk.Entry(master=window, fg='white', bg='purple', width=50)
entry1.pack()
entry1.insert(tk.END, 'A po lun me pupca?')

window.mainloop()