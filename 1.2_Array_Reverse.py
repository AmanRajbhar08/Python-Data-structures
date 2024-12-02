#initalizing the array with size of 5
numbers=[0]*5

#loop to take the input of 5 numbers 
for i in range(len(numbers)):
    numbers[i]=int(input(f"Enter the {i+1} element of array "))

# loop to access the the numbers by their index positions.
print("Oiginal Array :")
for i in range(len(numbers)):
    print(numbers[i],end=" ") 
print()     
    
# loop to reverse the array 
print("Reversed Array :")
for i in range(len(numbers)-1,-1,-1):
    print(numbers[i],end=" ")    