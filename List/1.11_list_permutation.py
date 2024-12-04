def permutation(lst):
    """
    def:function to generate permutation and combination 

    Args:
        lst (int): list of integer

    Returns:
        list of permutation: all the possible permutation
    """
    # Base case: if the list is empty, return a list containing an empty list
    if len(lst) == 0:
        return [[]]
    
    # List to store permutations
    result = []
    
    # Iterate through each element in the list
    for i in range(len(lst)):
        # Select the current element
        m = lst[i]
        
        # Remaining list excluding the current element
        remain_list = lst[:i] + lst[i+1:]
        
        # Generate permutations for the remaining list
        for p in permutation(remain_list):
            # Append the current element to each permutation of the remaining list
            result.append([m] + p)
    
    return result

# sample list
sample_list = [1, 2, 3]

#print the permuation 
print(permutation(sample_list))
