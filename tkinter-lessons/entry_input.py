import tkinter as tk

window = tk.Tk()

label = tk.Label(master=window, text='Name')

entry = tk.Entry(
    master=window,
    fg='black',
    bg='white',
    width=50
)

def get_entry_text():
    print(entry.get())


def delete_entry_text():
    entry.delete(0, tk.END)


def insert_text():
    entry.insert(tk.END, 'Python')


button = tk.Button(master=window, text='Get entry text', command=get_entry_text)
button_delete = tk.Button(master=window, text='Delte entry text', command=delete_entry_text)
button_insert = tk.Button(master=window, text="Insert text", command=insert_text)


label.pack()
entry.pack()
button.pack()
button_delete.pack()
button_insert.pack()

window.mainloop()