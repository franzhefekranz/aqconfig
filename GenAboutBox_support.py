#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.10.1a1
# In conjunction with Tcl version 8.6
#    Feb 03, 2018 01:02:54 PM
#    Oct 20, 2020 01:04:01 PM CEST  platform: Windows NT
#    Oct 20, 2020 01:06:56 PM CEST  platform: Windows NT

#======================================================
#    GenAboutBox_support.py
#------------------------------------------------------
# Created for the Page Tutorial Project
# Written by G.D. Walters
# Copyright (c) 2018 by G.D. Walters
# This source code is released under the MIT License 
# (See MIT_License.txt)
#======================================================

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import webbrowser
import gettext
_ = gettext.gettext

def OnBtnDismiss(p1):
    print('GenAboutBox_support.OnBtnDismiss')
    sys.stdout.flush()
    root.withdraw()
    
def LoadForm():
    global temp
    copyright_symbol = u"\u00A9"
    w.lblProgName.configure(text = temp[0])
    w.lblAuthor.configure(text = "Written by {0}".format(temp[1]))
    w.lblVersion.configure(text = "Version {0}".format(temp[2]))
    w.lblCopyright.configure(text = temp[3])
    w.Scrolledtext1.insert(END,temp[4])
        
def init(top, gui, *args, **kwargs):
    global w, top_level, root, temp
    w = gui
    top_level = top
    root = top
    temp = list(args)[0]  
    LoadForm()

def lblHomepage_LeftClick(p1):
    webbrowser.open_new('https://www.taxis-instruments.de')


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import GenAboutBox
    GenAboutBox.vp_start_gui()




