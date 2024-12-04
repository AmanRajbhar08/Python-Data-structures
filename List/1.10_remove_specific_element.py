# Original list
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Create a new list excluding the 0th, 4th, and 5th elements
result_list = [item for index, item in enumerate(sample_list) if index not in [0, 4, 5]]

# Print the result
print(result_list)
