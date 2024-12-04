def lowercasr_n_char(string,n):
    """
    def: function to covenrt first n char to lower case 

    Args:
        string,
        n: number of char want to lower case

    Returns:
        string : string with first n char to lower and rest same.
    """
    lower_str=''
    for i in range(len(string)):
        if i<n:
            lower_str+=string[i].lower()
        else:
            lower_str+=string[i]    
        
    return lower_str

#sample string input 
sample_str=input("Enter a string :")

#input number of char you want to lower 
num=int(input("Enter the number of char you want to lower :"))

#calling the lower case method and print the return string 
print(lowercasr_n_char(sample_str,num))        
            
        
