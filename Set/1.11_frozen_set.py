# Create a frozenset .
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])

# Use the 'isdisjoint()' method to check if 'x' and 'y' have no common elements and print the result.
# Return True if the sets have no elements in common with each other.
print(x.isdisjoint(y))

# Use the 'difference()' method to find the elements in 'x' that are not in 'y' and print the result.
# Return a new frozenset with elements in 'x' that are not in 'y'.
print(x.difference(y))

# Create a new frozenset with elements that are a union of 'x' and 'y' and print the result.
# This combines elements from both 'x' and 'y'.
print(x | y) 
