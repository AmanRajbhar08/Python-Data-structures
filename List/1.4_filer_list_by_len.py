def filter_list(list):
    """
    def: function to filter the list by len more than 2 and first and lst char same 

    Args:
        list (int): numbers in list

    Returns:
        int: filtered list 
    """
    filterd_list=[]
    #iterarte and filter 
    for item in list:
        if len(item)>=2 and item[0]==item[-1]:
            filterd_list.append(item)
    return filterd_list


#input the number of item for list 
numbers=int(input("Enter the number of element you want to end in list : "))   

#initliase list 
list_of_num=[]

#list input 
for i in range(numbers):
    n=input()
    list_of_num.append(n)
print() 

#printing the filtered of list 
print(f"filtered list: {(filter_list(list_of_num))}")   
     
        
