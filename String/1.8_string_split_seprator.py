def string_split_specator(string,seprator):
    """
    def: funtion to get the last part of a string before a specified character.

    Args:
        string (string): stirng 
        seprator (string):"/"

    Returns:
        string : seprated string 
    """
    
    seprated_string=string.rsplit(f"{seprator}",1)[0]
    return seprated_string


#stirng ssample 
sample_str="https://www.w3resource.com/python-exercises"
#seprator to split with 
split_with="/"

#calling the string slit method and printing the return statment 
print(string_split_specator(sample_str,split_with)) 
