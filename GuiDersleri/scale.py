from tkinter import *

window =Tk()

def submit():
    print("the temparature is: "+str(scale.get())+" degrees C")

scale= Scale(window,
             from_=1000,
             to=0,
             length=600,
             orient=VERTICAL,
             font=("Consolas",20),
             tickinterval=10,
             #showvalue=0,
             resolution=5,)

scale.set(((scale["from"]-scale["to"])/2)+scale["to"])

scale.pack()

button=Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()