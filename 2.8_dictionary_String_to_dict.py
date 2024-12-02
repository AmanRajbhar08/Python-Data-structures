#given string to genrate the dict from string
Word_string="w3resource"

#empty dict to count the char occurance in the string 
string_count_dict={  
}

#generating the dict from string by counting the occurance of the string 
for c in Word_string:
    if c in string_count_dict:
        string_count_dict[c] +=1
    else:
        string_count_dict[c]=1


#printing the generated string         
print(string_count_dict)            
