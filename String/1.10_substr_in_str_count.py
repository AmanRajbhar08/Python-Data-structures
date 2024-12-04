def count_substr(string,substirng):
    """
    def: function to count the num of time a sub string occured in a stirng 

    Args:
        string (stirng)
        substirng (stirng)

    Returns:
       count of substirng 
    """
    count=string.count(substirng) 
    return count

#input a sample stirng 
sample_str=input("Enter a string word or stentance :")

#input the substirgn for count 
sub_string=input("Enter the sub string you want to count in string :")

#printing the no of time substirng occurent by calling count substring method
print(f"{sub_string} occured {count_substr(sample_str,sub_string)} times in the string {sample_str}")
