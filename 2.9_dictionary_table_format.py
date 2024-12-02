#input the number for table generation
n=int(input("Enter the number whoes table you want to print :"))

#initalising table dict
table_dict={
    
}

#generating the table dictionary 
for i in range(1,11):
    table_dict[i]=n*i

#printing the dict in the table format  
print(f"Table of {n} :")  
for key,value in table_dict.items():
    print(f"{n}  *  {key}   =  {value}")    
    


