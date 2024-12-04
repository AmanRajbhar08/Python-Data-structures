def min_in_list(list):
    """
    def: function to find min in list

    Args:
        list (int): numbers in list

    Returns:
        int: min in list 
    """
    #min assingn to first value initially
    minimum=list[0]
    #iterarte and check for minimum
    for item in list:
        if item<minimum:
            minimum=item
    return minimum


#input the number of item for list 
numbers=int(input("Enter the number of element you want to end in list : "))   

#initliase list 
list_of_num=[]

#list input 
for i in range(numbers):
    n=int(input())
    list_of_num.append(n)
print() 

#printing the minimum of list 
print(f"Minimum in List {min_in_list(list_of_num)}")   
     
        
