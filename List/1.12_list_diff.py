def check_differance(list1,list2):
    """def: Check the differance between two list

    Args:
        list1 (int): n num of int
        list2 (int): n num of int 

    Returns:
        list : differance between two list
    """
    #to store the element not in 2nd list
    first=[]
    #to store the element not in 1st list
    second=[]
    
    #adding the element misisng in first list
    for item1 in list1:
        if item1 not in list2:
            first.append(item1)
    #adding the element missing in second list
    for item2 in list2:
        if item2 not in list1:
            second.append(item2)
                               
    return first+second

#sample list 1
sample_list1=[1,2,3,4,5]
#sample list 2 
sample_list2=[2,3,4,5,6,7]   

#printing the differance between two list 
print(check_differance(sample_list1,sample_list2))         
