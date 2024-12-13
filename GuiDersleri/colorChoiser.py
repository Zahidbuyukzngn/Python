from tkinter import *
from tkinter import colorchooser

def click():
    color=colorchooser.askcolor()
    colorHex=color[1]
    window.config(bg=colorHex)
    #seçilen rengin # şeklindeki kodunu almış olduk
    print(color[1])

window=Tk()

window.geometry("420x420")
button=Button(text="Color Chooser",command=click)
button.pack()
window.mainloop()