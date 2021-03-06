#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#    Oct 20, 2020 01:06:48 PM CEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import os.path
from pathlib import Path
import os
import configparser
import gettext
# _ = gettext.gettext
gettext.install('GenAboutBox', 'locales')
cfg = Path(os.getcwd() + '\\config.ini')
if cfg.is_file():
    config = configparser.ConfigParser()
    config.optionxform = str

    try:
        config.read(cfg, encoding='utf-8')
    except BaseException:
        try:
            config.read(cfg, encoding='ANSI')
        except Exception as e:
            messagebox.showerror('Read config file', e)
    language = (config['aqconfig']['language'])

    if language == 'de':
        lng1 = gettext.translation('GenAboutBox', \
                                   localedir='locales', \
                                   languages=['de'])
        lng1.install()
        _ = lng1.gettext
    elif language == 'en':
        lng2 = gettext.translation('GenAboutBox', \
                                   localedir='locales', \
                                   languages=['en'])
        lng2.install()
        _ = lng2.gettext
    elif language == 'fr':
        lng3 = gettext.translation('GenAboutBox', \
                                   localedir='locales', \
                                   languages=['fr'])
        lng.install()
        _ = lng3.gettext

import GenAboutBox_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = About (root)
    GenAboutBox_support.init(root, top)
    root.mainloop()

def set_lng(language):
    ''' translate the app '''
    de = gettext.translation('GenAboutBox',\
                              localedir='locales',\
                              languages=['de'])
    de.install()
    _ = de.gettext


w = None
def create_About(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_About(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = About (w)
    GenAboutBox_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_About():
    global w
    w.destroy()
    w = None

class About:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("459x535+341+118")
        top.minsize(120, 1)
        top.maxsize(1265, 770)
        top.resizable(0,  0)
        top.title("About")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lblProgName = tk.Label(top)
        self.lblProgName.place(x=10, y=20, height=29, width=436)
        self.lblProgName.configure(activebackground="#f9f9f9")
        self.lblProgName.configure(activeforeground="black")
        self.lblProgName.configure(background="#d9d9d9")
        self.lblProgName.configure(disabledforeground="#a3a3a3")
        self.lblProgName.configure(foreground="#000000")
        self.lblProgName.configure(highlightbackground="#d9d9d9")
        self.lblProgName.configure(highlightcolor="black")
        self.lblProgName.configure(relief="sunken")
        self.lblProgName.configure(text='''Label''')

        self.lblVersion = tk.Label(top)
        self.lblVersion.place(x=10, y=52, height=29, width=436)
        self.lblVersion.configure(activebackground="#f9f9f9")
        self.lblVersion.configure(activeforeground="black")
        self.lblVersion.configure(background="#d9d9d9")
        self.lblVersion.configure(disabledforeground="#a3a3a3")
        self.lblVersion.configure(foreground="#000000")
        self.lblVersion.configure(highlightbackground="#d9d9d9")
        self.lblVersion.configure(highlightcolor="black")
        self.lblVersion.configure(relief="sunken")
        self.lblVersion.configure(text='''Label''')

        self.lblAuthor = tk.Label(top)
        self.lblAuthor.place(x=10, y=84, height=29, width=436)
        self.lblAuthor.configure(activebackground="#f9f9f9")
        self.lblAuthor.configure(activeforeground="black")
        self.lblAuthor.configure(background="#d9d9d9")
        self.lblAuthor.configure(disabledforeground="#a3a3a3")
        self.lblAuthor.configure(foreground="#000000")
        self.lblAuthor.configure(highlightbackground="#d9d9d9")
        self.lblAuthor.configure(highlightcolor="black")
        self.lblAuthor.configure(relief="sunken")
        self.lblAuthor.configure(text='''Label''')

        self.lblCopyright = tk.Label(top)
        self.lblCopyright.place(x=10, y=110, height=29, width=436)
        self.lblCopyright.configure(activebackground="#f9f9f9")
        self.lblCopyright.configure(activeforeground="black")
        self.lblCopyright.configure(background="#d9d9d9")
        self.lblCopyright.configure(disabledforeground="#a3a3a3")
        self.lblCopyright.configure(foreground="#000000")
        self.lblCopyright.configure(highlightbackground="#d9d9d9")
        self.lblCopyright.configure(highlightcolor="black")
        self.lblCopyright.configure(relief="sunken")
        self.lblCopyright.configure(text='''Label''')

        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(x=10, y=180, height=280, width=438)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="word")

        self.btnDismiss = tk.Button(top)
        self.btnDismiss.place(x=130, y=470, height=37, width=177)
        self.btnDismiss.configure(activebackground="#d9d9d9")
        self.btnDismiss.configure(activeforeground="black")
        self.btnDismiss.configure(background="#d9d9d9")
        self.btnDismiss.configure(disabledforeground="#a3a3a3")
        self.btnDismiss.configure(foreground="#000000")
        self.btnDismiss.configure(highlightbackground="#d9d9d9")
        self.btnDismiss.configure(highlightcolor="black")
        self.btnDismiss.configure(pady="0")
        self.btnDismiss.configure(text=_('''Dismiss'''))
        self.btnDismiss.bind('<Button-1>',lambda e:GenAboutBox_support.OnBtnDismiss(e))

        self.lblHomepage = tk.Label(top)
        self.lblHomepage.place(x=10, y=140, height=29, width=436)
        self.lblHomepage.configure(activebackground="#f9f9f9")
        self.lblHomepage.configure(activeforeground="black")
        self.lblHomepage.configure(background="#d9d9d9")
        self.lblHomepage.configure(disabledforeground="#a3a3a3")
        self.lblHomepage.configure(foreground="#0000ff")
        self.lblHomepage.configure(highlightbackground="#d9d9d9")
        self.lblHomepage.configure(highlightcolor="#000000")
        self.lblHomepage.configure(relief="sunken")
        self.lblHomepage.configure(text='''www.taxis-instruments.de''')
        self.lblHomepage.bind('<Button-1>',lambda e:GenAboutBox_support.lblHomepage_LeftClick("https://www.taxis-instruments.de"))

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





