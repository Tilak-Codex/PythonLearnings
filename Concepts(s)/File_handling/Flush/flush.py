                                                                    #flush()

"""
        Flush() flushes the write buffer.
        
        It is same as close() but keeps the file open for more writing

"""

f1=open("file.txt","w")
f1.write("hello i am trying to understand flush method")
f1.flush()

