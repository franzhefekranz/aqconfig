from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Style
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="#333")          
        self.parent = parent        
        self.parent.title("sample")
        # self.parent.iconbitmap('sample.ico')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()
    def centerWindow(self):      
        w = 500
        h = 450
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def closeBtn(self):
        '''creating Button to close window'''
        self.parent.style = Style()
        self.parent.style.theme_use("default")
        quitButton = Button(self.parent,text='Close',command=self.parent.destroy)
        quitButton.place(x=50,y=50)  
    def initUI(self):
        '''self.closeBtn()'''
        frame1=Frame(self)
        frame1.pack(fill=BOTH)
        ''' Operating system selection'''
        os_label = Label(frame1,text="Current OS :",width=10)
        os_label.pack(side=LEFT, padx=5, pady=5)
        '''os =[("Winows",1),
             ("Linux",2),
             ("Mac",3)
        ]'''
        v = IntVar()
        v.set(1) #Default value i.e. Windows
        '''for txt,val in os:
            radiobtn_os = Radiobutton(frame1,text=txt,variable=v,value=val).pack(side=LEFT, padx=5, pady=5)'''
        radiobtn_os1 = Radiobutton(frame1,text="Winows",variable=v,value=1)
        radiobtn_os1.pack(side=LEFT, padx=5, pady=5)
        radiobtn_os1.select()
        radiobtn_os2 = Radiobutton(frame1,text="Linux",variable=v,value=2)
        radiobtn_os2.pack(side=LEFT, padx=5, pady=5)
        radiobtn_os2.deselect()
        radiobtn_os3 = Radiobutton(frame1,text="Mac",variable=v,value=3)
        radiobtn_os3.pack(side=LEFT, padx=5, pady=5)
        radiobtn_os3.deselect()
        '''Drive selection'''
        frame2=Frame(self)
        frame2.pack(fill=BOTH)
        scan_label = Label(frame2,text="System Scan :",width=11).pack(side=LEFT, padx=5, pady=5)
        sscan =[("Default",1),
             ("Custom",2),
        ]
        w = IntVar()
        w.set(1) # Default value i.e. Windows
        for txt,val in sscan:
            radiobtn_scan = Radiobutton(frame2,text=txt,variable=w,value=val)
            radiobtn_scan.pack(side=LEFT, padx=5, pady=5)
def main():
    root = Tk()
    app = Example(root)
    root.mainloop()  
if __name__ == '__main__':
    main()