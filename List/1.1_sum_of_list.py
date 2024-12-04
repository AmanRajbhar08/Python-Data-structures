def sum_of_list(list):
    """
    def: function to calucmalte the sum of list

    Args:
        list (int): numbers in list

    Returns:
        int: sum of list
    """
    #sum intialize 0
    list_sum=0
    #iterarte and sum
    for item in list:
        list_sum += item
    return list_sum


#input the number of item for list 
numbers=int(input("Enter the number of element you want to end in list : "))   

#initliase list 
list_of_num=[]

#list input 
for i in range(numbers):
    n=int(input())
    list_of_num.append(n)
print() 

#printing the sum of list 
print(f"Sum of List {sum_of_list(list_of_num)}")   
     
        
