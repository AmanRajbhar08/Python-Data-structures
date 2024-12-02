#declaring the student marks dictionary  with key name and marks value
Student_marks = {
    "Aman": 40,
    "sam": 70,
    "rahul": 33,
    "vikas": 12,
    "gourav": 89
}

#printing orignal dictionary 
print(f"Original Dictionary :{Student_marks}")

#removing the key "rahul from orignal dict"
Student_marks.pop("rahul")

#printing the dict after the removal of key 
print(Student_marks)