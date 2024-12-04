#saple tuple with repatative element
sample_tuple = ( "boy", "apple", "boy", )

#printing the tuple intiallly
print(f"{sample_tuple}")

#input to find the element 
find=input("Enter the element you want to check if exit in tuple or not : ")

#initallay setting result False
result=False
for item in sample_tuple:
    if item==find:
        result=True

# Print repeated items
print("Exitance :",result )

