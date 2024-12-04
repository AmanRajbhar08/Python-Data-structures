def add_str_at_end(string):
    '''
    def: function to add Ing and ly at the ed of the string based to condition
    parameter: stirng
    return : new  string
    '''
    
    #empty string
    new_string=""
    #based of len adding ing and ly at the end of the stirng 
    if len(string)>=3 and string[-3:] !="ing":
        new_string =string+ "ing"
    elif len(string)>=3 and string[-3:] =="ing": 
        new_string=string +"ly"
    else:
        return string
           
    
    return new_string 
    
    
#enter the sample stirng 
sample_string=input("Enter a string :")


#calling the function and printing the return statment based on conditons 
print(add_str_at_end(sample_string))    
