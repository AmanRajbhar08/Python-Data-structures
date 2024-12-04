#function to sort the list in increaing order 
def sortlist_containg_tuple(list):
    """def: program to sort the list containg tuple by the last element of 
            the tuple in increaing order      

    Args:
        list (tuple): list containg tuple elements

    Returns:
       list: sorted in increasing order 
    """
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i][-1]>list[j][-1]:
                list[i],list[j]=list[j],list[i]
                
    return list
        
        
#list containing tuples             
list_with_tuples=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 

#printing the sorted list of tuple  
print(sortlist_containg_tuple(list_with_tuples))      