from tkinter import*

#Widgets -> GUI elements such as text boxes,labels,images...

#windows -> Serves as a container to hold these widgets.


root=Tk()  #Creates window

#Geometry
root.geometry("420x420") #Weightxheight of window
root.minsize(400,400) #This sets the min size of the window (Weight,height)
root.maxsize(600,600) #This sets the max size of the window (Weight,height)

#Label
My_label=Label(text="This is a label")#This will create a label but which has to be packed inorder to be displayed to the end user
My_label.pack()

root.title("My Window") #Changes the title but icon(feather) remains

root.mainloop()  #displayswindow and remembers the changes done to the window


