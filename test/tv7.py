import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import *
def parse_csv(content, delimiter = ';'):  ##We use here ";" to parse CSV because of the European way of dealing with excel-csv
  csv_data = []
  for line in content.split('\n'):
    csv_data.append( [x.strip() for x in line.split( delimiter )] ) # strips spaces also
  return csv_data

canvas=parse_csv(open('canvas.csv','rU',encoding="ISO-8859-1").read())
#fediaf_requirements is a list containing where fediaf has a 
fediaf_requirements=[]
for i in range(0,len(canvas)):
               if canvas[i][1]=="FEDIAF":
                  fediaf_requirements.append(canvas[i][0])

car_header = ['Used Nutrients in the Profession', 'Nutrients used in this PetFood (Source : Official Website)', 'FEDIAF Requirement']


#Create the Data to be put into the table
def FromCSV_to_Tree(liste_croq):
    global car_list
    car_list=[]
    value=str(liste_croq.get(liste_croq.curselection()))
    for i in range(0,len(Remplissage)):
               if Remplissage[i][0]=="Name":
                  for j in range(1,len(Remplissage[i])):
                      if Remplissage[i][j]==value:
                          for k in range(0,len(Remplissage)-1):
                              if Remplissage[k][0] in fediaf_requirements :
                                  a="Required"
                              else :
                                  a=""


                              if Remplissage[k][j]!="ND":
                                     car_list.append([Remplissage[k][0],"OK",a])
                              else:
                                  car_list.append([Remplissage[k][0],"",a])



def CurSelet_croq(evt,container):
    global car_list
    FromCSV_to_Tree(liste_croq)
    car_header = ['Used Nutrients in the Profession', 'Nutrients used in this PetFood (Source : Official Website)', 'FEDIAF Requirement']
    print(car_list)


    #create a treeview with dual scrollbars

    #Container and container.pack detached to update the tree with the new datas. 
    container.pack(fill='both', expand=True)




    tree = ttk.Treeview(columns=car_header, show="headings")
    vsb = ttk.Scrollbar(orient="vertical",
                        command=tree.yview)
    hsb = ttk.Scrollbar(orient="horizontal",
                        command=tree.xview)
    tree.configure(yscrollcommand=vsb.set,
                   xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew', in_=container)
    vsb.grid(column=1, row=0, sticky='ns', in_=container)
    hsb.grid(column=0, row=1, sticky='ew', in_=container)

    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    def sortby(tree, col, descending):
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(tree.set(child, col), child) \
            for child in tree.get_children('')]
        # if the data to be sorted is numeric change to float
        #data =  change_numeric(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        tree.heading(col, command=lambda col=col: sortby(tree, col, \

            int(not descending)))

##Put data into the tree
    for col in car_header:
        tree.heading(col, text=col.title(),
                     command=lambda c=col: sortby(tree, c, 0))
        # adjust the column's width to the header string
        tree.column(col,
                    width=tkFont.Font().measure(col.title()))

    for item in car_list:
        tree.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(val)
            if tree.column(car_header[ix],width=None)<col_w:
               tree.column(car_header[ix], width=col_w)










Remplissage=parse_csv(open('Remplissage.csv','rU',encoding="ISO-8859-1").read())
root = tk.Tk()
root.wm_title("Visualizer")

container = ttk.Frame()

liste_croq = Listbox(root,width=70, height=10)
for i in range(0,len(Remplissage)):
               if Remplissage[i][0]=="Name":
                  for j in range(1,len(Remplissage[i])):
                      liste_croq.insert(i,Remplissage[i][j])
                      liste_croq.bind('<<ListboxSelect>>', lambda evt, container=container : CurSelet_croq(evt,container))
                      liste_croq.pack()


root.mainloop()