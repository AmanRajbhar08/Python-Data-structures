#declaring the student marks dictionary  with key name and marks value
Student_marks = {
    "Aman": 40,
    "sam": 70,
    "rahul": 33,
    "vikas": 12,
    "gourav": 89
}


print("Iterating the Dictionary ")

#iterating the dictionary with key and values respectivly 
for key,value in Student_marks.items():
    print(f"key[Name] {key} : value[marks] {value}")
    
