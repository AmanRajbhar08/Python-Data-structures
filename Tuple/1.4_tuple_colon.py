from copy import deepcopy
#tuple cration with diff data types 
mix_tuple=(1,"Aman",[2],True)

print(f"Before colon {mix_tuple}")

#deepcopy the tuple into a new tuple
tuple_colon=deepcopy(mix_tuple)

#appending a num in list at 2nd index of the tuple 
tuple_colon[2].append(50)

#printing the tuple after appending 
print(f"After colon and apending a new element in tuple: {tuple_colon} ")







