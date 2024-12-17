from tkinter import *
from PIL import Image, ImageTk

def openFile():
    print ("file has been opened")

def saveFile():
    print ("file has been saved")

def cut():
    print ("you cut some text")

def copy():
    print ("you copied some text")

def paste():
    print ("you pasted some text")


window=Tk()

# Resimleri yükle ve yeniden boyutlandır
openImagePIL = Image.open("C:\\Users\\Zahid\\OneDrive\\Masaüstü\\YAZILIM\\Python\\GuiDersleri\\docfile.png")
openImagePIL = openImagePIL.resize((25, 25))  # Genişlik ve yükseklik

saveImagePIL = Image.open("C:\\Users\\Zahid\\OneDrive\\Masaüstü\\YAZILIM\\Python\\GuiDersleri\\save.png")
saveImagePIL = saveImagePIL.resize((25, 25))

exitImagePIL = Image.open("C:\\Users\\Zahid\\OneDrive\\Masaüstü\\YAZILIM\\Python\\GuiDersleri\\exit.png")
exitImagePIL = exitImagePIL.resize((25, 25))

# Yeniden boyutlandırılmış resimleri tkinter için uygun formata çevir
openImage = ImageTk.PhotoImage(openImagePIL)
saveImage = ImageTk.PhotoImage(saveImagePIL)
exitImage = ImageTk.PhotoImage(exitImagePIL)


menubar=Menu(window)
window.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openFile,image=openImage,compound=LEFT)
filemenu.add_command(label="Save",command=saveFile,image=saveImage,compound=LEFT)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit,image=exitImage,compound=LEFT)

editMenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()