# sample tuple 
tuplex = ("a", "b", "c", "d", "e", "f", "g", "h", "i","j")

print(f"Before removing any element : {tuplex}")

# Tuples are immutable, so you cannot remove elements directly.
# To "remove" an item, create a new tuple by merging the desired elements using the + operator.
tuplex = tuplex[:2] + tuplex[3:]
# Print the updated 'tuplex' tuple
print(tuplex)


