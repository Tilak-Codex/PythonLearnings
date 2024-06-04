from tkinter import *

root=Tk()



#Making Button to perform some action

def ClickMyButton():
    MyLabel=Label(root,text="I just clicked MyButton",fg="gold",font=("ariel",20,"bold  italic"))
    MyLabel.pack()
        #use command option in button

MyButton=Button(root,text="Click me",command=ClickMyButton,fg="gold",bg="black",font=("ariel",20,"bold  italic"))
MyButton.pack()


root.mainloop()



"""
BUTTON OPTIONS

state=DISABLED
padx=int
pady=int


"""
