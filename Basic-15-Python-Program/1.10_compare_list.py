#function two compare two list and print all the element that are not present in other list
def compare_list(list1,list2):
    '''
    def: compare two list to check the missing element in other list
    parameter: list1,list2
    return :list with missing element
    '''
    list3=[]
    for _ in list1:
        if _ not in list2:
            list3.append(_)
    return  list3


        
        
#list of elements        
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

#calling the compare list method and printing the remaining elements
print(compare_list(color_list_1,color_list_2))