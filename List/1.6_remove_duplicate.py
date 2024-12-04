#function to sort the list in increaing order 
def list_remove_duplicate(list):
    """def: remove duplicate from the list  
                  
    Args:
        list : list containg numbers repetative

    Returns:
       list: distinct list 
    """
    distinct=[]
    for _ in list:
        if _ not in distinct:
            distinct.append(_)
            
    return distinct
        
        
#list containing repative numbers         
sample_list=[1,2,3,43,4,4,42,43,3,5,8,9] 

#printing the distinct list
print(f"Orignal list:  {sample_list}")
print(f"After removing duplicate {list_remove_duplicate(sample_list)}")      
