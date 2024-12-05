#sample sets
sample_set1 =set([1,2,3])
sample_set2=set([1,2,3,5,6])

#empty set to store interset 
intersect=set()

#iternation to check intersect
for item1 in sample_set1:
    if item1 in sample_set2:
        intersect.add(item1)

#printing the interset         
print(f"Intersection of {sample_set1} and {sample_set2} is : {intersect}")        
