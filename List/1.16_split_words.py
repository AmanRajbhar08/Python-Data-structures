#Automatically initializes a list for each key when a new key is accessed.
from collections import defaultdict

def split_by_first_character(words):
    # Create a dictionary where keys are the first characters and values are lists of words
    grouped_words = defaultdict(list)
    
    for word in words:
        first_char = word[0].lower()  # Use lowercase to group case-insensitively
        grouped_words[first_char].append(word)
    
    return dict(grouped_words)

# Example usage
word_list = ["apple", "banana", "apricot", "blueberry", "cherry", "carrot", "Avocado"]
result = split_by_first_character(word_list)

# Print the result
for key, group in result.items():
    print(f"{key}: {group}")


