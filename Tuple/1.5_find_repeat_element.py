#saple tuple with repatative element
sample_tuple = (1, 1, 2, 3, 4, "boy", "apple", "boy", True, True)

# Find repeated items
repeated_items = set()
seen_items = set()

#iterating tuple  and filtering repetative
for item in sample_tuple:
    if item in seen_items:
        repeated_items.add(item)
    else:
        seen_items.add(item)

# Print repeated items
print("Repeated items:", repeated_items)
