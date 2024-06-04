from tkinter import *


root=Tk()

txtlabel=Label(root,text="Enter your name").grid(row=0,column=0)
e=Entry(root,width=15,bg="grey",fg="white",borderwidth=5)
e.grid(row=0,column=1)

e.insert(0,"Enter your name") #inserts a text in the entry

#we can get value using e.get()
def btnclick1():
        lb2=Label(root,text=e.get())
        lb2.grid(row=2,column=1)
#To delete the deafult text in entry when user clicks it
   
button=Button(root,text="Click to revele your age",borderwidth=5,padx=5,command=btnclick1).grid(row=1,column=1)

root.mainloop()


"""
Dont mix pack & grid in a master window

.grid() or .pack() returns None

.insert(o/END,"text")
"""
