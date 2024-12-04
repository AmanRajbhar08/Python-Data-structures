#sample Lists
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]


#converting into a single string seprated by comma
list2_str=' '.join(map(str,list2))


# Create a circular version of list1 and convert to a string:
list1_circular_str=' '.join(map(str,list1*2))


#checking if list2 string exit in list1 circular list 
result= list2_str in list1_circular_str

#print the result if it is criculary identical or not 
print(result)
    

