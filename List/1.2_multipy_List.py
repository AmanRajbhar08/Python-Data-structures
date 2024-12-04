def multiply_list(list):
    """
    def: function to multiply list 

    Args:
        list (int): numbers in list

    Returns:
        int: product of list
    """
    #product intialize 1
    list_product=1
    #iterarte and multiply
    for item in list:
        list_product *= item
    return list_product


#input the number of item for list 
numbers=int(input("Enter the number of element you want to end in list : "))   

#initliase list 
list_of_num=[]

#list input 
for i in range(numbers):
    n=int(input())
    list_of_num.append(n)
print() 

#printing the product of list 
print(f"product of List {multiply_list(list_of_num)}")   
     
        
