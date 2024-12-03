#function to print histogram that take list of integer as an argument 
def print_histogram(list):
    for j in range(len(list_of_integer)):
     for i in range(list_of_integer[j],0,-1):
       print("*",end="")
     print() 

#list of integer
list_of_integer=[7,3,4,5,3,8,4]
#calling hisogram function
print_histogram(list_of_integer)

   
    

