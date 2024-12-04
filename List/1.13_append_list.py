def append_list_A_on_B(list1,list2):
    """def:yo append list 2 on list 1

    Args:
        list1 (int): list of num
        list2 (int): list of num

    Returns:
        list : appended list2 on list1
    """
    for item in list2:
        list1.append(item)
    return list1 


#sample list 1 
sample_list1=[1,2,3,4,5]
#sample list 2
sample_list2=[6,7,8]

#print list 1 one which is appending list 2:
print(append_list_A_on_B(sample_list1,sample_list2))


   
        
        

