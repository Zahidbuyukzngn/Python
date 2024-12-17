from tkinter import *

def openFile():
    print ("file has been opened")

def saveFile():
    print ("file has been saved")

def cut():
    print ("you cut some text")

def copy():
    print ("you copied some text")

def paste():
    print ("you pasted some text")

window=Tk()

menubar=Menu(window)
window.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

editMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()