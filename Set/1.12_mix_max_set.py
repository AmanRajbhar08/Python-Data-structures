# Define a set with some values
numbers = {10, 20, 5, 40, 15}

# Initialize variables with extreme values
max_value = float('-inf')  # Smallest possible number
min_value = float('inf')   # Largest possible number

# Iterate through the set to find max and min
for number in numbers:
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

# Print the results
print("Maximum value in the set:", max_value)
print("Minimum value in the set:", min_value)

