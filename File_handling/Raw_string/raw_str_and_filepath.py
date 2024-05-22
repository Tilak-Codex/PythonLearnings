                                                                    #File path and raw string

"""
        Python interprets \ as escape squence to avoid this raw string is used
        raw sting can be created by -> using r before string declaration or using \\
"""

with open(r"C:\Users\DELL\Desktop\dummy\file1","w") as f1:   #paste the directory and dont forget to give \file name 
    print("file opened")
