from tkinter import *

window=Tk()

listbox=Listbox(window,
                )

listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Hamburger")
listbox.insert(4,"MeatBread")
listbox.insert(5,"Soup")




window.mainloop()