#initalizing the array with size of 5
numbers=[0]*5

#loop to take the input of 5 numbers 
for i in range(len(numbers)):
    numbers[i]=int(input(f"Enter the {i+1} element of array "))

# loop to acces the the numbers by their index positions.
for i in range(len(numbers)):
    print(f"[{i}] element of the array {numbers[i]}")  