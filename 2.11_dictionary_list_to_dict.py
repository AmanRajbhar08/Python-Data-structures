#list containing numbers from one to five that needs to be  converted into a dictionary
counting_numbers=[
    "one",
    "two",
    "three",
    "four",
    "five",
    ]

# empty dictionary that will be converted a list into dict
number_dict={
    
}

#iterating the list and associating the values from list to the keys i.e converting list into dict 
for i in range(len(counting_numbers)):
    number_dict[i+1]=counting_numbers[i]
    
#printing the converted dict.
print(number_dict)    
