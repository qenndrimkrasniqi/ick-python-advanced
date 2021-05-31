import tkinter as tk

window = tk.Tk()
text_box = tk.Text(master=window)
text_box.pack()


def get_text():
    text = text_box.get("1.0", "1.4")
    text2 = text_box.get("1.0", tk.END)
    print(text)
    print(text2)

def delete_text():
    text_box.delete('1.0', '1.4')


def insert_text():
    text_box.insert(tk.END, 'Hello')


button_get = tk.Button(master=window, text='Get text', command=get_text)
button_get.pack()

button_delete = tk.Button(master=window, text='Delete text', command=delete_text)
button_delete.pack()

button_insert = tk.Button(master=window, text='Insert text', command=insert_text)
button_insert.pack()

window.mainloop()
