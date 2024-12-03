#function to convert list into a string
def list_to_string(nums):
    string=" "
    #iterating each element form the lsit and converting it to str and concating it to string 
    for _ in nums:
        string +=str(_)
        
    return string

#list of Integer
list_of_int=[2,4,5,63,22,4]


#printing the coverted list after concatinating it to a string 
print(list_to_string(list_of_int))    
        
        
