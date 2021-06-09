import tkinter as tk

window = tk.Tk()
lbl_names = [
    'First Name', 'Last Name', 'Address Line1', 'Address line 2', 'City', 'State/Provice',
    'Postal Code', 'Country'
]

for indx, lbl_name in enumerate(lbl_names):
    tk.Label(master=window, text=f'{lbl_name}:').grid(row=indx, column=0)
    tk.Entry(master=window, width=50).grid(row=indx, column=1, columnspan=12)

tk.Button(master=window, text='Clear').grid(row=9, column=11)
tk.Button(master=window, text='Submit').grid(row=9, column=12)

window.mainloop()
