#Images are displayed using labels...

from PIL import Image,ImageTk
from tkinter import*

root=Tk()

photo=PhotoImage(file="1.png")
img_label=Label(image=photo)
img_label.pack()

#For jpg image
"""
image=Image.open("")
photo=ImageTk.PhotoImage(image)
img_label=Label(image=photo)
img_label.pack()
"""
root.mainloop()
