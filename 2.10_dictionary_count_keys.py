#declaring the dictionary sample data
sample_data=[
    {
    'id': 1, 
    'success': True,
    'name': 'Lary'
     },
    {
    'id': 2, 
    'success': False,
    'name': 'Rabi'
     },
    {
    'id': 3, 
    'success': True,
    'name': 'Alex'
    }
]

#initialising the counter with 0
count=0

#iterating the dictionary and checking for condition
for item in sample_data:
    if item["success"] == True:
        count +=1


#printing the counter number of time condition met
print(count)        
        

