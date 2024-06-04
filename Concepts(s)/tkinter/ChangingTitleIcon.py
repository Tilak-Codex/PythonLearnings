from tkinter import *
from PIL import Image,ImageTk

root=Tk()

#Changing Title
root.title("My Window")
root.geometry("400x400")

#Changing Icon

#1.If you have .ico image
#root.iconbitmap(r"C:\Users\DELL\Pictures\Saved Pictures\bubu-transparent.png")

#2.png image(import PIL)
img=Image.open(r"C:\Users\DELL\Pictures\Saved Pictures\bubu-transparent.png")
photo=ImageTk.PhotoImage(img)
root.wm_iconphoto(False,photo)

root.mainloop()
