def word_greater_than_n(list,n):
    """
    def:function to filter the list with word greater than n 

    Args:
        list (string ): list of words
        n (integer): length 

    Returns:
        list: containg words whoes len is greater than n
    """
    #empty list
    greater_list=[]
    #iterarte list and check with n len 
    for _ in list:
        if len(_) > n:
            greater_list.append(_)
    return greater_list


#sample list 
sample=["abc","umbrella","Mango","book","train","food","Macbook"]

#number to filter the list with word greater than n 
n=int(input("Enter a number n to filter the list with word greater than n :"))

#printing the words  greater than n
print(word_greater_than_n(sample,n))        
            
