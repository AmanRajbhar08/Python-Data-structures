# creating a set 
sample_set= {1,2,3,4,5}

print(f"Before adding an item to set {sample_set}")
#removing an item from  set 

#item to check if in set 
n=int(input("Enter an item to check in set and then remove it :"))

if n in sample_set:
    sample_set.remove(n)
else:
    print(f"{n} is not present in set")
        

#after removing an item from set 
print(f"set {sample_set}")

