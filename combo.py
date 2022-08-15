import tkinter as tk
from tkinter import ttk
import db

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
  
# label text for title
ttk.Label(window, text = "GFG Combobox Widget", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
  
# label
ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

data = db.getAddresses()
address_choices = []
for id, address in data:
    address_choices.append(address)
    print(id, address)

# Adding combobox drop down list
monthchoosen['values'] = address_choices
  
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
window.mainloop()