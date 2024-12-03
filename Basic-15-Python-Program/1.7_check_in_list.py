#group of numbers
numbers=[1,3,4,5,10,66,5,44,4,3]

#element you want to check exits or not
n=int(input("Enter the number you want to check in number : "))

#checking the exitance of number
if n in numbers:
  print(f"Yes {n} is present in the group number {numbers}")
else:
  print(f"No {n} do not exit is {numbers}")    
