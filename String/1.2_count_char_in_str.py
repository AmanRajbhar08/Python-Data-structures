#function to count the char in a string
def count_char_of_str(string):
    '''
    def:count char in a string 
    parameter: string 
    return :dictionary 
    '''
    #dict to store the count of char
    count_str={}
    
    #loop to iterarte the string and count the occurance 
    for i in range(len(string)):
        if string[i]in count_str:
            count_str[string[i]] +=1
        else:
            count_str[string[i]] =1 
            
    return count_str;
 
#smaple string            
str1=input("Enter a string :")

#calling the function count string 
print(count_char_of_str(str1))            