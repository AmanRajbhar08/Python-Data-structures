def longest_word_in_list(lis):
    """
    def: function to count the longest wornd in the given list

    Args:
        list :containg stings

    Returns:
        len of longest string, and string itself
    """
    #longest word 
    longest_length_word=0
    #iterate the list and find the largest string 
    for _ in lis:
        if len(_) > longest_length_word:
            longest_length_word =len(_)
    return  _,longest_length_word,

#smaple list containg words
sample_list=["Amb", "umbrella", "apple","bank","opportunity"]

#unpacking the the result into a list 
[word, length ]=longest_word_in_list(sample_list)  

#print statement for the output 
print(f"Longest word in the list is {word} with length {length}")    