# Define a tuple
sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing examples
sliced_tuple_1 = sample_tuple[2:6]  # Get elements from index 2 to 5
sliced_tuple_2 = sample_tuple[:4]   # Get the first 4 elements
sliced_tuple_3 = sample_tuple[5:]   # Get elements from index 5 to the end
sliced_tuple_4 = sample_tuple[::2]  # Get every second element
sliced_tuple_5 = sample_tuple[::-1] # Reverse the tuple

# Print results
print("Original tuple:", sample_tuple)
print("Sliced tuple (index 2 to 5):", sliced_tuple_1)
print("Sliced tuple (first 4 elements):", sliced_tuple_2)
print("Sliced tuple (from index 5 to end):", sliced_tuple_3)
print("Sliced tuple (every second element):", sliced_tuple_4)
print("Reversed tuple:", sliced_tuple_5)

