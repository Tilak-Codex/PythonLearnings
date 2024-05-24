                                                            #File Handling
#Why File ?
"""
To store data permanently we use Files
Files are stored in secondary memory which is non-volatile
Genrally files are used to give large input to a program
Files are used to store the output of a program permanently also
"""
#File is a sequence of bytes

#Types of file
"""
1. Text file (.txt,.csv)
2.Binary files
(store img,videos,exe file)
"""
#Sequence of operation
""" Open -> Read -> Write -> close """


#Opening a file

#open("filename","mode")
""" Returns a file object which can be assigned to a var
       All the operations on file are done using this reference
"""
"""
  Modes -> r , r+ , w , w+ , a , a+
  For binary files use rb , wb  ..,
"""

#For opening a file it must exist in the memory if a non exisitng file is opened in read mode we get filenotfound error

#To create a file in current working directory we can use x mode

#f1=open("file1.txt","x")
"""
    We can see in the cwd, the following filr file1.txt is created, but when this statement is executed again, itraises fileexist error
    so this mode can be used to create a file only when the file does not already exist
    Also we can use w mode to create a new file
"""
#f1=open("file1.txt","w")    # The file pointer will move to the begining of the file, earsing all the content in the file.


#Reading a file
f1=open("file1.txt","r")

"""
 When a file is opened in r mode,
         the file pointer is placed in the beginging of the file
         If file doesnot exist it rasies I/O error
         It the the default mode for opening a file
"""
#using read(size)

data=f1.read()     #Reads the entire file
#print(data)

#Now again reading the whole file
data1=f1.read()
#print(data1)       #nothing is printed because file pointer is the the end.
f1.seek(0)

#Using readline(size) -> No.of bytes to return from a line

#,print(f1.readline(2))      #First line is fetched
#print(f1.readline(3))      #Second line is fetched
#print(f1.readline())      #Third line is fetched
f1.seek(0)

#Using readlines(lines) -> Returns a list containing each line in the file as a list item. Default value is -1
#print(f1.readlines()) 


#WRITE MODE
"""
        w mode is used to add contents to the file at the begining.
        if nonexisting file is given new file is created"
"""

#write(bytes)
#f1=open("file1.txt","w")
#str="India is a secular state where all religions are equal \n one can follow any religion on his own will."
#f1.write(str)
#f1.close()    #The content will be written into to the file only after it is closed.
"""
        If w is given old content is deleted and new content is written
        if  a  is given new content is added to the end of old content
"""
#writelines(list) ->Adds the elements of the list to a file.
l=["hello","my","name","is"]   #like  generally comma is not printed as space so we have to give space and \n for newlline
#f1.writelines(l)
#f1.close()
