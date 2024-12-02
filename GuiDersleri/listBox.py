from tkinter import *

def submit():
    print("You have ordered: ")
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
    
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())



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



entrybox=Entry(window,
              )
entrybox.pack()



submitbutton=Button(window,
              text="SUBMİT",
              command=submit)
submitbutton.pack()



addbutton=Button(window,
                 text="ADD",
                 command=add)
addbutton.pack()


deletebutton=Button(window,
                 text="DELETE",
                 command=delete)
deletebutton.pack()

window.mainloop()