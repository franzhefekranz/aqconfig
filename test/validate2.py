import tkinter as tk
import tkvalidate as v
root = tk.Tk()
widget = tk.Entry(root, justify=tk.CENTER)
widget.pack(padx=10, pady=10)
v.int_validate(widget, from_=-5, to=5)
root.mainloop()