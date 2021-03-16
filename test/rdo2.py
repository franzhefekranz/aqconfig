import tkinter as tk
import tkinter.ttk as ttk
 
root = tk.Tk()
vstring = tk.IntVar()
values = [
    ("option 1"),
    ("option 2"),
    ("option 3"),
    ("option 4")
]
 
for v in values:
	# Here is the ttk style widget
    rb = ttk.Radiobutton(root,
        text=v,
        value= v[-1],
        variable = vstring)
    rb.pack(anchor=tk.W)
 
root. mainloop()