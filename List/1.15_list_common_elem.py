def check_common(list1,list2):
    """def: Check the common between two list

    Args:
        list1 (int): n num of int
        list2 (int): n num of int 

    Returns:
        list : common in two list
    """
    #list to store the common lement in both list
    common=[]
    
   #checking if the elemnt are common in both list
    for item in list1:
        if item in list2:
            common.append(item)
    return common

#sample list 1
sample_list1=[1,2,3,4,5]
#sample list 2 
sample_list2=[2,3,4,5,6,7]   

#printing the common between two list 
print(check_common(sample_list1,sample_list2))         
