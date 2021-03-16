import sys
from sqlite3 import *
import datetime
import sys

try:
    import Tkinter # as tk
except ImportError:
    import tkinter # as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
try:
    from Tkinter import *
    import tkMessageBox
except ImportError:
    from tkinter import *
    from tkinter import messagebox
try:
    import Queue
except ImportError:
    import queue
# from Tkinter import *
# import ttk
# import tkMessageBox
# import Queue
   
class QueueTest:
    def __init__(self,master = None):
        self.DefineVars()
        f = self.BuildWidgets(master)
        self.PlaceWidgets(f)
        self.ShowStatus()
        self.LastQueue = 'fifo'
    
    def DefineVars(self):
        self.QueueType = ''
        self.LastQueue = ''
        self.FullStatus = StringVar()
        self.EmptyStatus = StringVar()
        self.Item = StringVar()
        self.Output = StringVar()
        # Define the queues
        self.fifo = queue.Queue(10)
        self.lifo = queue.LifoQueue(10)
        self.pq = queue.PriorityQueue(10)
        self.obj = self.fifo
        
    def BuildWidgets(self,master):
        # Define our widgets
        frame = Frame(master)
        self.f1 = Frame(frame, 
            relief = SUNKEN,
            borderwidth=2,
            width = 300,
            padx = 3,
            pady = 3
        )
        self.btnFifo = Button(self.f1,
            text = "FIFO"
        )    
        #
        self.btnFifo.bind('<Button-1>',
            lambda e: self.btnMain(1)
        )        
        self.btnLifo = Button(self.f1,
            text = "LIFO"
        )    
        self.btnLifo.bind('<ButtonRelease-1>',
            lambda e: self.btnMain(2)
        )
        self.btnPriority = Button(self.f1,
            text = "PRIORITY"
        )    
        self.btnPriority.bind('<ButtonRelease-1>',
            lambda e: self.btnMain(3)
        )
        self.f2 = Frame(frame, 
            relief = SUNKEN,
            borderwidth=2,
            width = 300,
            padx = 3,
            pady = 3
        )
        self.txtAdd = Entry(self.f2,
            width=5,
            textvar=self.Item
        )
        self.txtAdd.bind('<Return>',self.AddToQueue)
        self.btnAdd = Button(self.f2,
            text='Add to Queue',
            padx = 3,
            pady = 3
        )
        self.btnAdd.bind('<ButtonRelease-1>',self.AddToQueue)
        self.btnGet = Button(self.f2,
            text='Get Next Item',
            padx = 3,
            pady = 3
        )
        self.btnGet.bind('<ButtonRelease-1>',self.GetFromQueue)
        self.lblEmpty = Label(self.f2,
            textvariable=self.EmptyStatus,
            relief=FLAT
        )
        self.lblFull = Label(self.f2,
            textvariable=self.FullStatus,
            relief=FLAT
        )
        self.lblData = Label(self.f2,
            textvariable=self.Output,
            relief = FLAT,
            font=("Helvetica", 16),
            padx = 5
        )

        return frame
        
    def PlaceWidgets(self, master):
        frame = master
        # Place the widgets
        frame.grid(column = 0, row = 0)
        l = Label(frame,text='',relief=FLAT,width = 15, anchor = 'e').grid(column = 0, row = 0)
        l = Label(frame,text='',relief=FLAT,width = 15, anchor = 'e').grid(column = 1, row = 0)
        l = Label(frame,text='',relief=FLAT,width = 15, anchor = 'e').grid(column = 2, row = 0)
        l = Label(frame,text='',relief=FLAT,width = 15, anchor = 'e').grid(column = 3, row = 0)
        l = Label(frame,text='',relief=FLAT,width = 15, anchor = 'e').grid(column = 4, row = 0)
                                       
        self.f1.grid(column = 0,row = 1,sticky='nsew',columnspan=5,padx = 5,pady = 5) 
        l = Label(self.f1,text='',width = 25,anchor = 'e').grid(column = 0, row = 0)
        self.btnFifo.grid(column = 1,row = 0,padx = 4)
        self.btnLifo.grid(column = 2,row = 0,padx = 4)
        self.btnPriority.grid(column = 3, row = 0, padx = 4)
        self.f2.grid(column = 0,row = 2,sticky='nsew',columnspan=5,padx = 5, pady = 5) 
        l = Label(self.f2,text='',width = 15,anchor = 'e').grid(column = 0, row = 0)
        self.txtAdd.grid(column=1,row=0)
        self.btnAdd.grid(column=2,row=0)
        self.btnGet.grid(column=3,row=0)
        self.lblEmpty.grid(column=2,row=1)
        self.lblFull.grid(column=3,row = 1)
        self.lblData.grid(column = 4,row = 0)

    def Quit(self):
        sys.exit()
    
    def btnMain(self,p1):
        if p1 == 1:
            self.QueueType = 'FIFO'
            self.obj = self.fifo
            root.title('Queue Tests - FIFO')
            #self.btnFifo.config(relief='sunken')
        elif p1 == 2:
            self.QueueType = 'LIFO'
            self.obj = self.lifo
            root.title('Queue Tests - LIFO')
        elif p1 == 3:
            self.QueueType = 'PRIORITY'
            self.obj = self.pq
            root.title('Queue Tests - Priority')
        elif p1 == 4:
            self.QueueType = 'RING'
        print(self.QueueType)
        self.ShowStatus()
        
    def ShowStatus(self):
        # Check for Empty
        if self.obj.empty() == True:
            self.EmptyStatus.set('Empty')
        else:
            self.EmptyStatus.set('')
        # Check for Full
        if self.obj.full() == True:
            self.FullStatus.set('FULL')
        else:
            self.FullStatus.set('')
            
    def AddToQueue(self,p1):
        temp = self.Item.get()
        if self.QueueType == 'PRIORITY':
            commapos = temp.find(',')
            if commapos == -1:
                print("ERROR")
                tkMessageBox.showerror('Queue Demo',
                    'Priority entry must be in format\r(priority,data)')
            else:
                self.obj.put(self.Item.get())
        elif not self.obj.full():
            self.obj.put(self.Item.get())
        self.Item.set('')
        self.ShowStatus()
        
    def GetFromQueue(self,p1):
        self.Output.set('')
        if not self.obj.empty():
            temp = self.obj.get()
            self.Output.set("Pulled {0}".format(temp))
        self.ShowStatus()

            
if __name__ == '__main__':
    def Center(window):
        # Get the width and height of the screen
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()        
        # Get the width and height of the window
        rw = window.winfo_reqwidth()
        rh = window.winfo_reqheight()
        xc = (sw-rw)/2
        yc = (sh-rh)/2
        window.geometry("%dx%d+%d+%d"%(rw,rh,xc,yc))
        window.deiconify()
    
    root = Tk()
    #root.withdraw()   
    root.title('Queue Tests - FIFO')
    demo = QueueTest(root)   
    root.after(3,Center,root)
    root.mainloop()