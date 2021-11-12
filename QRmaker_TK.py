# import the tkinter
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
import qrcode

# make the root
root = Tk()
root.geometry("500x500")
root.title("QRmaker")
root.iconbitmap("qr.ico")

# define a font
title_font = Font(
    family="Bahnschrift Light Condensed",
    size=20,
    weight="bold"
)
def click(event):
    entry1.config(state=NORMAL)
    entry1.delete(0, END)
label1 = Label(root, text="QR Maker...", pady=20, font=title_font)
label1.grid(row=0, column=0,columnspan = 2)
entry1 = Entry(root, width=30, borderwidth=3)
entry1.grid(row=1, column=0,columnspan = 2)
entry1.insert(0, "Click Delete than Enter the URL")
entry1.config(state=DISABLED)
entry1.bind("<Button-1>", click)


def QRmaker():
    global my_img
    URL = entry1.get()
    img = qrcode.make(URL)
    img.save("photo.png")
    my_img = ImageTk.PhotoImage(Image.open("photo.png"))
    img_label.config(image=my_img)



makeQR_button = Button(root, command=QRmaker, text="Make a QR img", padx=10,pady=5).grid(row=2, column=0)

my_img = ImageTk.PhotoImage(Image.open("photo.png"))
img_label = Button(root, image=my_img)
img_label.grid(row=4, column=0)

root.mainloop()
