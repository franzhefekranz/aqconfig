import tkinter as tk
from tkinter import ttk
import tkvalidate as validate

root = tk.Tk()
widget = ttk.Spinbox(root, justify=tk.CENTER, from_=-5, to=5)
widget.pack(padx=10, pady=10)
int_validate(widget)
root.mainloop()