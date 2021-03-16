import tkinter
import tkinter.ttk as ttk
root = tkinter.Tk()
master = tkinter.Frame(root)
master.pack()
tree = ttk.Treeview(master, columns=['col A','col B','col C'])
tree.pack()
row1 = tree.insert("",index=0,text="row1",values=['A1','B1','C1'])
row1  # 'I001'
row2 = tree.insert("",index=0,text="row2",values=['A2','B2','C2'])
row2  # 'I002'
row3 = tree.insert("",index=0,text="row3",values=['A3','B3','C3'])
row3  # 'I003'
root.mainloop()