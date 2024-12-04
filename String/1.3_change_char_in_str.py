def replace_char_in_Str(string,replace_char):
    '''
    def: function to replace a strings first occurance with $ expect the very first occurance 
    parameter: string, string needs to be replace
    return : string with replaced char
    '''
    #empty string
    new_string=''
    #count for replacing char
    count=0
    #iterarting the stirng and replacing it 
    for _ in string:
        if _ == replace_char:
            count +=1
            if count == 2:
              new_string += "$"
            else:
             new_string += _
              
        else:
            new_string += _
    return new_string


#input sample string 
sample_string=input("Enter a string :")

#input the char needs to be repalced
change_char=input("Enter the charater you want to replace :")

#calling the replace method and printing the return statement
print(replace_char_in_Str(sample_string,change_char))           
        
    
        
    
