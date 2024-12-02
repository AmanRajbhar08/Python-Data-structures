def sort_assending(dict): 
  '''
    def:function to sort the disctory in assending order
    parameter:dictionary
    return :sort dictionary in assending order
  ''' 
  # Convert dictionary into a list of (key, value) pairs
  items = list(Student_marks.items())

    # Sort the items based on the value using Bubble Sort
  for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:  # Compare values
            items[j], items[j + 1] = items[j + 1], items[j]

    # Create a new sorted dictionary
  sorted_dict = {}
  for key, value in items:
    sorted_dict[key] = value
    
  return sorted_dict  
        
def sort_desending(dict):
  '''
    def:function to sort the disctory in desending order
    parameter:dictionary
    return :sort dictionary in desending order
  '''   
  # Convert dictionary into a list of (key, value) pairs
  items = list(Student_marks.items())

    # Sort the items based on the value using Bubble Sort
  for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] < items[j + 1][1]:  # Compare values
            items[j], items[j + 1] = items[j + 1], items[j]

    # Create a new sorted dictionary
  sorted_dict = {}
  for key, value in items:
    sorted_dict[key] = value
    
  return sorted_dict  



#declaring the dictinary  student marks
Student_marks = {
    "Aman": 40,
    "sam": 70,
    "rahul": 33,
    "vikas": 12,
    "gourav": 89
}



# Print the sorted dictionary
print("Original Dictionary",Student_marks)
print("Sorted Dictionary in Assending order:",sort_assending(Student_marks))
print("Sorted Dictionary in Assending order:",sort_desending(Student_marks))
