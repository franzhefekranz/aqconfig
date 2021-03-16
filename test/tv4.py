import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('320x240')
tk.Label(root,text='tkinter treeview widget').pack()
area=('#', 'Northern Europe', 'Eastern Europe', 'Southern Europe', 'Western Europe', 'USA', 'Canada', 'Australia')

ac=('all','n','e','s','ne','nw','sw','c')
sales_data=[('Electronics','47814','41443','4114','14314','413','14314','84387'),
            ('Cosmetics','48349','94734', '4743','43434','43844','43843','88844'),
            ('Clothing','14841','49761', '147471','49094' ,'57844', '48499','49494'),
            ('Misc','4939','43934','43993','6894', '39933','3903','4344')
            ]

tv=ttk.Treeview(root,columns=ac,show='headings',height=7)
for i in range(8):
    tv.column(ac[i],width=70,anchor='e')
    tv.heading(ac[i],text=area[i])
tv.pack()

for i in range(4):
    tv.insert('','end',values=sales_data[i])
root.mainloop()