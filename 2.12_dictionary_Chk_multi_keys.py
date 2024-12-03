#sample dictionary with multiple similar keys
sample_dictionary={
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E"
    
}

key_list=list(sample_dictionary.keys())
count=0
#dictionary to count keys that occur multiple times 
for _ in sample_dictionary:
    count +=1
    
if count >1:
    print(f"Yes, there are multiple keys in the dictionary {count} diffrent keys {key_list} ") 
elif count==1:
    print(f"This dictionary have only single key {key_list}")
else:
    print(f"This is an empty list")           

        
            



