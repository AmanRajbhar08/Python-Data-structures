#no of elements you want to enter
n=int(input("Enter the no. of num you want to enter: "))

#input of sequence
num_list=[]
num_tuple=()
num = [int(num) for num in input(f"Enter a sequare of {n} number :").split(",")]

#converting the sequency in tuple and list
num_list=list(num) 
num_tuple=tuple(num)

#printing the output 
print(f"{num_list} - type : {type(num_list)}  ") 
print(f"{num_tuple} -type : {type(num_tuple)} ")
    

