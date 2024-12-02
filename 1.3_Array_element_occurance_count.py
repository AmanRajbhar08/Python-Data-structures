#initalizing the array with size of 5
numbers=[0]*5
searched_element=0
#loop to take the input of 5 numbers 
for i in range(len(numbers)):
    numbers[i]=int(input(f"Enter the {i+1} element of array "))

# loop to access the the numbers by their index positions.
print("Oiginal Array :")
for i in range(len(numbers)):
    print(numbers[i],end=" ") 
print()  

#user input of element whoes occurance we want to count
print("Enter the Element whoes occurance you want to count for the array :")
searched_element=int(input("Enter the Number:"))

   
    
# counting the occurance of searched element
# count initalize to zero
count=0
print(f"occurrences of {searched_element} in an array:")
for i in range(len(numbers)):
    if numbers[i]== searched_element:
        count+=1

#printing the final outcome 
print(f"{searched_element} occured {count} times in the array ")          