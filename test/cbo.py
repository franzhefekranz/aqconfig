import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

class Example:

  def __init__(self,master):
     self.master = master

     self.db = sqlite3.connect('stockdbExample.db')

     # use only once
     self.create_db()   

     self.cb = ttk.Combobox(master)
     self.cb.pack()
     self.cb['values'] = self.combo_input()

  def combo_input(self):
    cursor = self.db.cursor()

    cursor.execute('SELECT item FROM stocks')

    data = []

    for row in cursor.fetchall():
        data.append(row[0])

    return data

  def create_db(self):

    cursor = self.db.cursor()
    cursor.execute('CREATE TABLE stocks (item text)')
    cursor.execute('INSERT INTO stocks (item) VALUES("Hello")')
    cursor.execute('INSERT INTO stocks (item) VALUES("World")')
    cursor.execute('INSERT INTO stocks (item) VALUES("Tkinter")')
    cursor.close()

    self.db.commit()

root = tk.Tk()
Example(root)
root.mainloop()