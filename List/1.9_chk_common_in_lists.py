def check_common_in_list(list1,list2):
    """
    def: function to check even if one element is same in the list

    Args:
        list1 (int), list2 (int)

    Returns:
       common check (Boolean) : return ture if even one element is common in both lists
    """
    #common check 
    commom_check=False
    #iterarting the both list and commapring to check if any element is common 
    for item1 in list1:
        for item2 in list2: 
            if item1 == item2:
                commom_check=True
    return commom_check

#sample list 1
sample_list1=[1,2,4,3,5,]

#sample list 2
sample_list2=[14,12,8,6,15,11]

#printing the boolean it anything common in both the lists
print(check_common_in_list(sample_list1,sample_list2))           
