def unique_words_in_list(list):
    """def:function to return only uniuq words from the list 

    Args:
        list: containg words as string 

    Returns:
        list: only uniuq element in the list 
    """
    #empty list for unique element
    unique_list=[]
    #iterating the list and appending the unique elements
    for _ in list:
        if _ not in unique_list:
            unique_list.append(_)
            
    return unique_list

#sample List for input 
sample_list=[]

#input number of element for the list 
n=int(input("Enter the number of words you want in the list : "))

print(f"Enter {n} string for a list :")
#input for words in the list 
for i in range(n):
    sample_stirng=input()  
    sample_list.append(sample_stirng)
  
#printing the final output     
print(f" {unique_words_in_list(sample_list)}")          
