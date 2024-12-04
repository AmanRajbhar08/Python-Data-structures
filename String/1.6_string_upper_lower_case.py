def string_upper_lower(string):
    """
    def: progrma to reversea string and return its upper and lower string 

    Args:
        string 

    Returns:
        reverse upper string, reverse lower string 
    """
    #reverse the string 
    reverse_str=string[::-1]
    #return reverse with upper and lower case repectivly 
    return reverse_str.upper(),reverse_str.lower()

#input sample string 
sample_string=input("Enter a stirng :")

#unpacking the reverse upper and lower string 
upper_str, lower_str =string_upper_lower(sample_string)


#print the output 
print(f" string reverse Upper : {upper_str} and reverse Lower {lower_str}")
