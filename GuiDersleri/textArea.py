from tkinter import *

def submit():
    imput=text.get("1.0",END)   
    print(imput)

    
window=Tk()
    
text=Text(window,
          font=("Ink Free",25),
          bg="light yellow",
          width=30,
          height=15,
          padx=30,
          pady=30,
          fg="purple")
text.pack()

button=Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()