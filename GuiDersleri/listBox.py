from tkinter import *

def submit():
    print("You have ordered: ")
    print(listbox.get(listbox.curselection()))


window=Tk()

listbox=Listbox(window,
                bg=("#f7ffde"),
                font=("constantia",35),
                width=12
                )

listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Hamburger")
listbox.insert(4,"MeatBread")
listbox.insert(5,"Soup")

listbox.config(height=listbox.size())

button=Button(window,
              text="submit",
              command=submit)

button.pack()

window.mainloop()