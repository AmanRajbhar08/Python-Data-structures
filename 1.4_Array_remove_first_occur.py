# Initializing the array with a size of 5
numbers = [0] * 5

# Loop to take input of 5 numbers
for i in range(len(numbers)):
    numbers[i] = int(input(f"Enter the {i+1} element of the array: "))

# Printing the array
print("Array before removal:")
for num in numbers:
    print(num, end=" ")
print()

# Taking input for the number to remove
removing_num = int(input("Enter the number whose first occurrence you want to remove from the array: "))

# Remove the first occurrence of the number in the array
if removing_num in numbers:
    numbers.remove(removing_num)  # Directly removes the first occurrence of the number
else:
    print(f"The number {removing_num} is not in the array.")

# Printing the array after removal
print(f"Array after removing the first occurrence of {removing_num}:")
for num in numbers:
    print(num, end=" ")
print()
