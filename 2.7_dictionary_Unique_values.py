#Declaring the sample data for dictionary with key and values 
Sample_Data={
    "V":"S001", 
    "V": "S002",
    "VI": "S001",
    "VI": "S005",
    "VII":"S005", 
    "V":"S009",
    "VIII":"S007"
}

#initalising the empty unique dictonary
unique_data={    
}
#printing the original dictionary
print(f"orignal Dictionary {Sample_Data}")

#removing the duplicate values from the dict and keep only unique data
for key,value in Sample_Data.items():
    if key not in unique_data:
        unique_data.update({key:value})
        

#printing the unique values in the dictionary 
print(f"unique values {unique_data}")
