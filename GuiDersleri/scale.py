from tkinter import *

window =Tk()

def submit():
    print("the temparature is: "+str(scale.get())+" degrees C")

scale= Scale(window,from_=100,to=0,)
scale.pack()

button=Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()