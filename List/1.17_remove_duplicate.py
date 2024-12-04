#function to sort the list in increaing order 
def remove_duplicate(list):
    """def: program to remove duplicate  the list containg tuple  
                  

    Args:
        list (tuple): list containg tuple elements

    Returns:
       list: distict list with tuple  
    """
    #to store the distinct tuples
    distinct_list=[]
    #adding the distinct elemnt to the distinct list 
    for item in list:
        if item not in distinct_list:
            distinct_list.append(item)
                   
    return distinct_list
        
        
#list containing tuples             
list_with_tuples=[(10, 20), (40), (30, 56, 25), (10, 20), (33), (40)] 

#printing the distinct list of tuple  
print(remove_duplicate(list_with_tuples))      
