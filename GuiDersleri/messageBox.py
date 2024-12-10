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
    "evet veya hayır cevabı almak için kullanıcıya sorduk"
    # if messagebox.askyesno(title="ask yes or no",message="do you like etliekmek??"):
    #     print("yes, you like etliekmek")
    # else:
    #     print("no, you don't like etliekmek")

    "turta sever misin sorusu ile kullanıcıdan evet hayır girdisi aldık"
    # answer=messagebox.askquestion(title="ASK QUESTION",message="do you like pie!")
    # if answer=="yes":
    #     print("you like pie!")
    # else:
    #     print("you don't like pie!")

    "evet veya hayır veya iptal cevabı almak için kullanıcıya sorduk"
    "icon ile mesajımızın yanındaki ikonu değiştirebiliriz"
    answer=messagebox.askyesnocancel(title="yes no cancel",message="do you like to coding???",icon="warning")
    if answer==True:
        print("yes, you like coding!")
    elif answer==False:
        print("no, you don't like coding!")
    else:
        print("you have dodged the question! ")
button=Button(window,command=click,text="Click me")

button.pack()

window.mainloop()