from tkinter import *
from tkinter import messagebox

window=Tk()

def click():
    "show info ile sen bir insansın bilgisi verildi"
    #messagebox.showinfo(title="this is an info message box",message="you are a person ")
    "while ile sonsuz döngü vererek virüs var uyarısı verdirdik... Döngünün kapanması için kodu değiştir:)"
    #while(True):
     #messagebox.showwarning(title="WARNING!",message="YOU HAVE A VIRUS!!!")
    "hata kutusu oluşturduk"
    #messagebox.showerror(title="ERROR!",message="Something went wrong...")

    "kullanıcıya tamam iptal kutusu oluşturduk"
    # if messagebox.askokcancel(title="as ok cancel",message="do you want to do the think??"):
    #     print("you did a thing!")
    # else:
    #     print("you canceled a thing!")

    "tekrar dene kutusu oluşturduk"
    # if messagebox.askretrycancel(title="as ok cancel",message="do you want retry the thing??"):
    #     print("you retried a thing!")
    # else:
    #     print("you canceled a thing!")

    
button=Button(window,command=click,text="Click me")
button.pack()

window.mainloop()