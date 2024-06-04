from tkinter import *

root=Tk()

MyLabel1=Label(root,text="Hello Row1")
MyLabel2=Label(root,text="Hello Row2")
MyLabel3=Label(root,text="Hello Row3")

MyLabel1.grid(row=1,column=0)
MyLabel2.grid(row=2,column=10)
MyLabel3.grid(row=0,column=2)
#MyLabel1.pack()
#MyLabel2.pack()  #pack does in center


root.mainloop()
