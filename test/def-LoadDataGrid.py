def LoadDataGrid():
    """
    ###############################################################################
    # load values into the data treeview
    ###############################################################################
    """
    global ColHeads
    ClearDataGrid()
    records =[]
    # w.stwList.tag_configure('odd', background='#E8E8E8')
    # w.stwList.tag_configure('even', background='#DFDFDF')
    for c in range(100):
        name = 'Name ' + str(c)
        area = 'DB' +str(c) +'.DF' + str(2*c)
        gain = '1'
        offset = '0'
        unit = 'm³'
        record =[name, area, gain, offset,unit]
        records.append(record)
        
    for c in range(len(records)):
        # if (c%2)== 1:
            # w.stwList.insert('','end',c,text=str(c+1),values=records[c],tags = ('odd',))
        # else:
            # w.stwList.insert('','end',c,text=str(c+1),values=records[c],tags = ('even',))
        w.stwList.insert('','end',c,text=str(c+1),values=records[c])
            
        
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(ColHeads):
            if (py3 == 1) or (py3 == True):
                col_w = font.Font().measure(val)
            else:
                col_w = tkFont.Font().measure(val)
            if w.stwList.column(ColHeads[ix],width=None)<col_w:
                w.stwList.column(ColHeads[ix], width=col_w, achor='e')

