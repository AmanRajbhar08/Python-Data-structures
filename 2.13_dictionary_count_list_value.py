#sample dictinory with values as List 
sample_dict={
    1:["Apple","bat","book","bottel"],
    2:["red","Blue","Green","Yellow","Orange"],
    3:["Dog","Cat","horse","cow","Zerbra","lion","tiger"],     
}

#empty dictionary to count the value(list)
count_values={  
}

#iterating the dict with key, values and counting the item in the value that is a list
for key,value in sample_dict.items():
    count_values[key]=len(value)

#printing the item count alone with their associated keys     
print(count_values)    
    
    
