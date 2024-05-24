def operate():
    print("The operating function is beingexecuted")
    def execute():
        print("The execute function is being exeuted")
        
    return execute           #To parenthesis is used when return another function as value


result=operate()     #Now result fuction has the execute function

result()          #We are callling execute function using result()

#Result is reference to inner function called result


