                                                                    #Opening file using with

"""
        When open() is used to open a file it has to be closed explicitly
        But when file is opened using with the file is closed implicitly
        Because with calls 2 bultin methods behind the scene __enter()__ and __exit()__
        __exit()__ closes the file automatically once the specified operation is done
"""

with open("file2.txt","w") as f1:
    f1.write("hello this is a text file.")
