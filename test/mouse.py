from tkinter import *
import tkinter

top = tkinter.Tk()

B1 = tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="man")
B2 = tkinter.Button(top, text ="plus", relief=RAISED,\
                         cursor="question_arrow")
B1.pack()
B2.pack()
top.mainloop()