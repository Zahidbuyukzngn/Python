from tkinter import *

def submit():
    imput=text.get("1.0",END)   
    print(imput)

    
window=Tk()
    
text=Text(window)
text.pack()

button=Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()